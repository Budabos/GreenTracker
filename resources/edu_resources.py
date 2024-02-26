from flask_restful import Resource, reqparse
from models import Education_Resources
from config import db
from flask import request

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
        parser.add_argument('image_url', required=True, type=str, help='Image url is required')
        
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
        
class EduResourceById(Resource):
    def get(self, id):
        found_resource = Education_Resources.query.filter(Education_Resources.id == id).first()
        
        if not found_resource:
            return {
                "message":"Educational resource not found"
            },404
            
        return found_resource.to_dict(),200
    
    def patch(self, id):
        found_resource = Education_Resources.query.filter(Education_Resources.id == id).first()
        
        if not found_resource:
            return {
                "message":"Educational resource not found"
            },404
            
        for attr in request.json:
            if hasattr(found_resource, attr):
                setattr(found_resource, attr, request.json[attr])
            else:
                return {
                    "message": f"Invalid attribute '{attr}' provided"
                }, 400
            
        try:
            db.session.add(found_resource)
            db.session.commit()
            return {
                "message": "Education resource updated successfully",
                "resource": found_resource.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {
                "message": "An error occurred while updating the resource",
                "error": str(e)
            }, 500
    
        
    def delete(self, id):
        found_resource = Education_Resources.query.filter(Education_Resources.id == id).first()
        
        if not found_resource:
            return {
                "message":"Educational resource not found"
            },404
            
        db.session.delete(found_resource)
        db.session.commit()
        
        return {
            "message":"Educational resource delete successfully"
        },204