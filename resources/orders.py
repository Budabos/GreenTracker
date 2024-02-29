from flask import request
from flask_restful import Resource, reqparse
from models import OrderProduct, Products, Order, Users
from config import db

class Orders(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('product_ids', required=True, help='Product IDs is required')
        parser.add_argument('quantities', required=True, help='Quantities  is required')
        parser.add_argument('total_price', type=int, required=True, help='Total price is required')
        
        args = parser.parse_args()
        
        product_ids = [int(x) for x in args['product_ids'].split(',')]
        quantities = [int(x) for x in args['quantities'].split(',')]
        
        
        order = Order(user_id=args['user_id'], total_price=args['total_price'])
        db.session.add(order)
        db.session.commit()
        
        found_user = Users.query.filter(Users.id == args['user_id']).first()
        
        for product_id, quantity in zip(product_ids, quantities):
            found_product = Products.query.filter(Products.id == product_id).first()
            print(found_product)
            
            if not found_product:
                return {
                    "message":"Product not found"
                }, 404
             
                
            order_product = OrderProduct(order_id=order.id, product_id=found_product.id, quantity=quantity)
            
            db.session.add(order_product)
            
        db.session.commit()
            
        return {
            "message":"Order made successfully",
            "updated_user":found_user.to_dict()
        }, 200