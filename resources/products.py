from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models import Products
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

class ProductResource(Resource):
    @jwt_required()
    def get(self):
        products = [product.to_dict() for product in Products.query.all()]
        return products,200
    
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('price', type=int, required=True, help='Price is required')
        parser.add_argument('eco_rating', type=int, required=True, help='Eco-rating is required')
        parser.add_argument('image_url', required=True, type=str, help='Image url is required')
        
        
        args = parser.parse_args()
        
        new_product = Products(**args)
        db.session.add(new_product)
        db.session.commit()
        
        return {
            "message":"Product added successfully",
            "product":new_product.to_dict()
        }
        
class ProductResourceById(Resource):
    @jwt_required()
    def get(self, id):
        found_product = Products.query.filter(Products.id == id).first()
        
        if not found_product:
            return {
                "message":"Product not found"
            },404
            
        return found_product.to_dict(),200
    
    @jwt_required()    
    def delete(self, id):
        found_product = Products.query.filter(Products.id == id).first()
        
        if not found_product:
            return {
                "message":"Product not found"
            },404
            
        db.session.delete(found_product)
        db.session.commit()
        
        return {
            "message":"Product deleted successfully"
        },204
        
    @jwt_required()    
    def patch(self, id):
        found_product = Products.query.filter(Products.id == id).first()
        
        if not found_product:
            return {
                "message": "Product not found"
            }, 404

        if not request.json:
            return {
                "message": "No data provided in the request"
            }, 400
        
        for attr in request.json:
            if hasattr(found_product, attr):
                setattr(found_product, attr, request.json[attr])
            else:
                return {
                    "message": f"Invalid attribute '{attr}' provided"
                }, 400
                
        try:
            db.session.add(found_product)
            db.session.commit()
            return {
                "message": "Product updated successfully",
                "product": found_product.to_dict()
            }
        except Exception as e:
            db.session.rollback()
            return {
                "message": "An error occurred while updating the product",
                "error": str(e)
            }, 500