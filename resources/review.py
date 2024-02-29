from flask import request, jsonify
from flask_jwt_extended import jwt_required
from config import app, db
from models import Products, Reviews
from flask_restful import Resource, reqparse

class ReviewsResource(Resource):
    @jwt_required()
    def get(self):
        reviews = [review.to_dict() for review in Reviews.query.all()]
        return reviews
    
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('product_id', type=int, required=True, help='Product ID is required')
        parser.add_argument('rating', type=int, required=True, help='Rating is required')
        parser.add_argument('review_text', type=str, required=True, help='Review text is required')
            
        args = parser.parse_args()
        
        new_review = Reviews(**args)
        db.session.add(new_review)
        db.session.commit()
        
        return {
            "message":"Review posted successfully"
        }