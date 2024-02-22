from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from models import Partners

# Define PartnerResource class to handle partner requests
class PartnerResource(Resource):
    # POST method to create a new partner
    def post(self):
        # Create a request parser to parse incoming data
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('contact_info', type=str, required=True)
        parser.add_argument('website', type=str, required=True)
        args = parser.parse_args()
        
    # Create a new partner object with parsed data
        new_partner = Partners(
            name=args['name'],
            description=args['description'],
            contact_info=args['contact_info'],
            website=args['website']
        )
# Add the new partner to the database session and commit the transaction
        db.session.add(new_partner)
        db.session.commit()

        return {'message': 'Partner Request created successfully'}, 201
# Add the PartnerResource to the API at the specified endpoint
api.add_resource(PartnerResource, '/partners')

# Create database tables if they don't exist and run the Flask app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
