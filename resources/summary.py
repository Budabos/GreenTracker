from flask_restful import Resource
from models import Users, Products, Events, UserEvents

class Summary(Resource):
    def get(self):
        num_of_users = Users.query.count()
        num_of_products = Products.query.count()
        num_of_events = Events.query.count()
        num_of_bookings = UserEvents.query.count()
        
        categories = set([category.category for category in Products.query.with_entities(Products.category).all()])
    
        category_stats = []
        
        for category in categories:
            category_stats.append({
                "category":category,
                "count":Products.query.filter(Products.category == category).count()
            })
        
        return {
            "users":num_of_users,
            "products":num_of_products,
            "events":num_of_events,
            "bookings":num_of_bookings,
            "category_stats":category_stats
        }, 200