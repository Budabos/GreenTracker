from flask_restful import Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from models import Partners


class PartnerResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('contact_info', type=str, required=True)
        parser.add_argument('website', type=str, required=True)
        args = parser.parse_args()

        new_partner = Partners(
            name=args['name'],
            description=args['description'],
            contact_info=args['contact_info'],
            website=args['website']
        )

        db.session.add(new_partner)
        db.session.commit()

        return {'message': 'Partner Request created successfully'}, 201


