from flask_restful import Resource, reqparse
from models import Users
from config import db, bcrypt, jwt
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return Users.query.filter_by(id = identity).first().to_dict()


class UserAccounts(Resource):    
    def get(self):
        users = [user.to_dict() for user in Users.query.all()]
        
        return users,200
    
class SignUp(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('first_name', type=str, required=True, help='First name is required')
        parser.add_argument('last_name', type=str, required=True, help='Last name is required')
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('phone', type=str, required=True, help='Phone number is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        parser.add_argument('gender', type=str, required=True, help='Gender is required')
        parser.add_argument('status', required=True, help='Status is required')
        parser.add_argument('role', required=True, help='Role is required')
        parser.add_argument('interests', required=True, help='Interests is required')
        parser.add_argument('age', required=True, help='Age is required')
        
        args = parser.parse_args()
        
        found_user = Users.query.filter(Users.email == args['email']).first()
        
        if found_user:
            return {
                "message":"User already exists"
            },409
        
        args['password'] = generate_password_hash(args['password']).decode('utf-8')
        
        new_user = Users(**args)
        db.session.add(new_user)
        db.session.commit()
        
        #Generate token and return user dict
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)
        
        return {
            "message":"User created successfully",
            "access_token":access_token,
            "refresh_token":refresh_token,
            "user":new_user.to_dict()
        },201
        
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