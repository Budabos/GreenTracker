from flask_restful import Resource
from models import Users, Products, Events, UserEvents

class Summary(Resource):
    def get(self):
        num_of_users = Users.query.count()
        num_of_products = Products.query.count()
        num_of_events = Events.query.count()
        num_of_bookings = UserEvents.query.count()
        
        return {
            "users":num_of_users,
            "products":num_of_products,
            "events":num_of_events,
            "bookings":num_of_bookings
        }, 200