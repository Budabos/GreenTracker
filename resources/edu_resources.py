from flask_restful import Resource, reqparse
from models import Education_Resources
from config import db

class EduResource(Resource):
    def get(self):
        resources = [rec.to_dict() for rec in Education_Resources.query.all()]
        
        return resources,200
    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('content', type=str, required=True, help='Content is required')
        parser.add_argument('author', type=str, required=True, help='Author is required')
        parser.add_argument('date_published', required=True, help='Date published is required')
        parser.add_argument('image_url', required=True, type=str, help='Image url is required')
        
        
        args = parser.parse_args()
        
        new_edu_resource = Education_Resources(**args)
        db.session.add(new_edu_resource)
        db.session.commit()
        
        return {
            "message":"Education resource created successfully"
        }, 201