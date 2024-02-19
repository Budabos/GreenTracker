from flask import request, jsonify
from config import app, db
from models import Products, Review

@app.route('/products/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    output = []
    for review in reviews:
        review_data = {
            'id': review.id,
            'product_id': review.product_id,
            'rating': review.rating,
            'comment': review.comment
        }
        output.append(review_data)
    return jsonify({'reviews': output})

@app.route('/products/<int:product_id>/reviews', methods=['POST'])
def add_review(product_id):
    data = request.json
    new_review = Review(
        product_id=product_id,
        rating=data['rating'],
        comment=data['comment']
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'})

@app.route('/products/<int:product_id>/reviews/<int:review_id>', methods=['PUT'])
def update_review(product_id, review_id):
    review = Review.query.filter_by(product_id=product_id, id=review_id).first_or_404()
    data = request.json
    review.rating = data['rating']
    review.comment = data['comment']
    db.session.commit()
    return jsonify({'message': 'Review updated successfully'})

@app.route('/products/<int:product_id>/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(product_id, review_id):
    review = Review.query.filter_by(product_id=product_id, id=review_id).first_or_404()
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'})
