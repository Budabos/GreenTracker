from flask_restful import Resource, reqparse
from models import Education_Resources
from config import db

class EduResource(Resource):
    # GET method to fetch all education resources
    def get(self):
        # Retrieve all education resources from the database and convert them to dictionaries
        resources = [rec.to_dict() for rec in Education_Resources.query.all()]
        
        # Return the resources along with a success status code
        return resources,200
    
    # POST method to create a new education resource
    def post(self):
        # Create a request parser to parse incoming data
        parser = reqparse.RequestParser()
        
        # Add expected arguments to the parser
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('content', type=str, required=True, help='Content is required')
        parser.add_argument('author', type=str, required=True, help='Author is required')
        parser.add_argument('date_published', required=True, help='Date published is required')
        
        # Parse the arguments from the request
        args = parser.parse_args()
        
        # Create a new education resource object
        new_edu_resource = Education_Resources(**args)
        
        # Add the new resource to the database session and commit the transaction
        db.session.add(new_edu_resource)
        db.session.commit()
        
        # Return a success message along with a success status code
        return {
            "message":"Education resource created successfully"
        }, 201