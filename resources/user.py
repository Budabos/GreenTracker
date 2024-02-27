from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_mail import Mail, Message
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
from models import Users
from config import db

app = Flask(__name__)

# Setup Flask-Mail
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'c3bd45c5a3ecd2'
app.config['MAIL_PASSWORD'] = 'fd9e0258a34ec0'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Setup Flask-JWT-Extended
jwt = JWTManager(app)

# Setup Flask-Restful
api = Api(app)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return Users.query.filter_by(id=identity).first().to_dict()

class SendWelcomeMail:
    @staticmethod
    def send(email, first_name):
        try:
            msg = Message(subject='Welcome to GreenTracker!', sender='peter@mailtrap.io', recipients=[email])
            msg.body = f"Hey, welcome to GreenTracker! We're excited to have you on board, {first_name}!"
            mail.send(msg)
            print("Welcome email sent successfully")
        except Exception as e:
            print(f"Error sending welcome email: {str(e)}")

class UserAccounts(Resource):
    def get(self):
        # Retrieve all users from the database and convert them to dictionary format
        users = [user.to_dict() for user in Users.query.all()]
        return users, 200

class SignUp(Resource):
    def post(self):
        # Create a request parser to parse incoming data
        parser = reqparse.RequestParser()

        parser.add_argument('first_name', type=str, required=True, help='First name is required')
        parser.add_argument('last_name', type=str, required=True, help='Last name is required')
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('phone', type=str, required=True, help='Phone number is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        parser.add_argument('gender', type=str, required=True, help='Gender is required')
        parser.add_argument('image_url')
        parser.add_argument('role', required=True, help='Role is required')
        parser.add_argument('interests', required=True, help='Interests is required')
        parser.add_argument('age', required=True, help='Age is required')

        args = parser.parse_args()

        found_email = Users.query.filter(Users.email == args['email']).first()
        found_phone = Users.query.filter(Users.email == args['phone']).first()

        if found_email or found_phone:
            return {
                "message": "User already exists"
            }, 409

        args['password'] = generate_password_hash(args['password']).decode('utf-8')

        new_user = Users(**args)
        
        # Add the new user to the database session and commit the transaction
        db.session.add(new_user)
        db.session.commit()

        # Send welcome email using the SendWelcomeMail class
        SendWelcomeMail.send(args['email'], args['first_name'])

        # Generate token and return user dict
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        return {
            "message": "User created successfully",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": new_user.to_dict()
        }, 201

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        
        args = parser.parse_args()
        
        found_user = Users.query.filter(Users.email == args['email']).first()

        if not found_user or not check_password_hash(found_user.password, args['password']):
            return {
                "message":"Invalid credentials"
            },401
            
        #Generate token and return user dict
        access_token = create_access_token(identity=found_user.id)
        refresh_token = create_refresh_token(identity=found_user.id)
            
        return {
            "message":"Login successful",
            "access_token":access_token,
            "refresh_token":refresh_token,
            "user":found_user.to_dict()
        },200

class UserById(Resource):
    def get(self, id):
        found_user = Users.query.filter(Users.id == id).first()
        
        if not found_user:
            return {
                "message":"User not found"
            },404
            
        return found_user.to_dict(), 200
    
    def patch(self, id):
        found_user = Users.query.filter(Users.id == id).first()
        
        if not found_user:
            return {
                "message":"User not found"
            },404
            
        if request.json['phone'] or request.json['email']:
            found_phone = Users.query.filter(Users.id != found_user.id).filter(Users.phone == request.json['phone']).first()
            found_email = Users.query.filter(Users.id != found_user.id).filter(Users.email == request.json['email']).first()
            
            if found_phone:
                return {
                    "message":"Phone number already registered"
                }, 409
            elif found_email:
                return {
                    "message":"Email already registered"
                }, 409
            
        for attr in request.json:
            if attr != 'password':
                setattr(found_user, attr, request.json[attr])
            
        db.session.add(found_user)
        db.session.commit()
        
        return {
            "message":"User edited successfully",
            "user":found_user.to_dict()
        }
        
    def delete(self, id):
        found_user = Users.query.filter(Users.id == id).first()
        
        if not found_user:
            return {
                "message":"User not found"
            },404
            
        db.session.delete(found_user)
        
        return {
            "message":"User deleted successfully"
        },204
        
class ChangePassword(Resource):
    def patch(self, id):
        parser = reqparse.RequestParser()
        
        parser.add_argument('current_password', type=str, required=True, help='Current password is required')
        parser.add_argument('new_password', type=str, required=True, help='New password is required')
        
        args = parser.parse_args()
        
        found_user = Users.query.filter(Users.id == id).first()
        
        if not found_user:
            return {
                "message":"User not found"
            },404
        elif not check_password_hash(found_user.password, args['current_password']):
            return {
                "message":"Invalid credentials"
            },401
            
        args['new_password'] = generate_password_hash(args['new_password']).decode('utf-8')
            
        setattr(found_user, 'password', args['new_password'])
        
        db.session.add(found_user)
        db.session.commit()
        
        return {
            "message":"Password changed successfully"
        },200
