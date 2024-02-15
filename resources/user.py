from flask_restful import Resource, reqparse
from models import Users
from config import db, bcrypt

class UserAccounts(Resource):    
    def get(self):
        users = [user.to_dict() for user in Users.query.all()]
        
        return users,200
    
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
        
        args['password'] = bcrypt.generate_password_hash(args['password'].encode('utf-8'))
        
        new_user = Users(**args)
        db.session.add(new_user)
        db.session.commit()
        
        return {
            "message":"User created successfully"
        },201
        