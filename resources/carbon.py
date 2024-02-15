# Import necessary modules
from flask_restful import Resource, reqparse,fields
from models import db, CarbonFootPrintCountModel


#This dictionary defines the fields associated with a CarbonFootPrintCount resource.
CarbonFootPrintCount_fields = {
    "id": fields.Integer,
    "user_id":fields.Integer,
    "carbon_value": fields.String,
    "date": fields.String,
}

# Define a class named CarbonFootPrintCount that inherits from Resource
class CarbonFootPrintCount(Resource):
    # Initialize a request parser to parse incoming request data
    carbon_footprint_parser = reqparse.RequestParser()

    # Define the arguments expected in the request
    carbon_footprint_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
    carbon_footprint_parser.add_argument('carbon_value', type=str, required=True, help='Carbon value is required')
    carbon_footprint_parser.add_argument('date', type=str)

    # Define a post method to handle POST requests
    def post(self):
        # Parse the arguments from the request
        args = self.carbon_footprint_parser.parse_args()

        # Create a new instance of CarbonFootPrintCountModel with parsed arguments
        new_footprint = CarbonFootPrintCountModel(
            user_id=args['user_id'],
            carbon_value=args['carbon_value'],
            date=args.get('date') 
        )

        try:
            # Add the new instance to the database session
            db.session.add(new_footprint)

            # Commit the changes to the database
            db.session.commit()

            # Return a success message and status code 201
            return {'message': 'Carbon footprint count created successfully'}, 201
        except Exception as e:
            # If there's an error, rollback changes and return an error message with status code 500
            db.session.rollback()
            return {'error': 'An error occurred while creating carbon footprint count'}, 500
        
        
        
        
        
        # examples of other methods
    # def get(self, footprint_id):
    #     footprint = CarbonFootPrintCount.query.get(footprint_id)
    #     if footprint:
    #         return {'user_id': footprint.user_id, 'carbon_value': footprint.carbon_value, 'date': footprint.date}
    #     else:
    #         return {'error': 'Carbon footprint count not found'}, 404

    # def put(self, footprint_id):
    #     args = self.parser.parse_args()
    #     footprint = CarbonFootPrintCount.query.get(footprint_id)
    #     if footprint:
    #         footprint.user_id = args['user_id']
    #         footprint.carbon_value = args['carbon_value']
    #         footprint.date = args.get('date')
    #         db.session.commit()
    #         return {'message': 'Carbon footprint count updated successfully'}, 200
    #     else:
    #         return {'error': 'Carbon footprint count not found'}, 404

    # def delete(self, footprint_id):
    #     footprint = CarbonFootPrintCount.query.get(footprint_id)
    #     if footprint:
    #         db.session.delete(footprint)
    #         db.session.commit()
    #         return {'message': 'Carbon footprint count deleted successfully'}, 200
    #     else:
    #         return {'error': 'Carbon footprint count not found'}, 404

        

    





