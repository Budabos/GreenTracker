from flask_restful import Resource, reqparse
from models import Partners
from config import db

# Define PartnerResource class to handle partner requests
class PartnerResource(Resource):
    def get(self):
        partners = [partner.to_dict() for partner in Partners.query.all()]
        
        return partners
    
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

        return {'message': 'Partner created successfully'}, 201
