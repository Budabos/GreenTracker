from flask import request, jsonify
from config import app, db
from models import Products, Reviews
from flask_restful import Resource, reqparse

class ReviewsResource(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Reviews.query.all()]
        return reviews
    
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


# @app.route('/products/<int:product_id>/reviews', methods=['GET'])
# def get_reviews(product_id):
#     reviews = Reviews.query.filter_by(product_id=product_id).all()
#     output = []
#     for review in reviews:
#         review_data = {
#             'id': review.id,
#             'product_id': review.product_id,
#             'rating': review.rating,
#             'comment': review.comment
#         }
#         output.append(review_data)
#     return jsonify({'reviews': output})

# @app.route('/products/<int:product_id>/reviews', methods=['POST'])
# def add_review(product_id):
#     data = request.json
#     new_review = Reviews(
#         product_id=product_id,
#         rating=data['rating'],
#         comment=data['comment']
#     )
#     db.session.add(new_review)
#     db.session.commit()
#     return jsonify({'message': 'Review added successfully'})

# @app.route('/products/<int:product_id>/reviews/<int:review_id>', methods=['PUT'])
# def update_review(product_id, review_id):
#     review = Reviews.query.filter_by(product_id=product_id, id=review_id).first_or_404()
#     data = request.json
#     review.rating = data['rating']
#     review.comment = data['comment']
#     db.session.commit()
#     return jsonify({'message': 'Review updated successfully'})

# @app.route('/products/<int:product_id>/reviews/<int:review_id>', methods=['DELETE'])
# def delete_review(product_id, review_id):
#     review = Reviews.query.filter_by(product_id=product_id, id=review_id).first_or_404()
#     db.session.delete(review)
#     db.session.commit()
#     return jsonify({'message': 'Review deleted successfully'})
