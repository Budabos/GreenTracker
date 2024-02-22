from flask_restful import Resource, reqparse
from models import Users
from config import db, bcrypt

# Define UserAccounts class to handle user accounts
class UserAccounts(Resource): 
    
    # GET method to fetch all users   
    def get(self):
        # Retrieve all users from the database and convert them to dictionary format
        users = [user.to_dict() for user in Users.query.all()]
        
         # Return the list of users along with a success status code
        return users,200
    
    # POST method to create a new user
    def post(self):
        # Create a request parser to parse incoming data
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
        
        # Parse the incoming data
        args = parser.parse_args()
        
        # Hash the password using bcrypt before storing in the database
        args['password'] = bcrypt.generate_password_hash(args['password'].encode('utf-8'))
        
        # Create a new user object with parsed data
        new_user = Users(**args)
        
        # Add the new user to the database session and commit the transaction
        db.session.add(new_user)
        db.session.commit()
        
        # Return success message along with a success status code
        return {
            "message":"User created successfully"
        },201
        