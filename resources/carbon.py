# Import necessary modules
from flask_restful import Resource, reqparse,fields
from models import db, CarbonFootPrintCount

# Define fields for CarbonFootPrintCount
CarbonFootPrintCount_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "carbon_value": fields.String,
    "date": fields.String
}

# Define a class named CarbonFootPrintCount that inherits from Resource
class CarbonFootprintCalculation(Resource):
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
        new_footprint = CarbonFootPrintCount(
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
            return {'error': 'An error occurred while creating carbon footprint count'}, 500 
        
   

    # Define a get method to handle GET requests for retrieving a specific footprint
    def get(self, footprint_id):
        # Retrieve the carbon footprint record from the database by its ID
        footprint = CarbonFootPrintCountModel.query.get(footprint_id)
        if footprint:
            # If the footprint exists, return its details
            return {'user_id': footprint.user_id, 'carbon_value': footprint.carbon_value, 'date': footprint.date}
        else:
            # If the footprint does not exist, return an error message with status code 404
            return {'error': 'Carbon footprint count not found'}, 404

    # Define a put method to handle PUT requests for updating a specific footprint
    def put(self, footprint_id):
        # Parse the request arguments to extract user input
        args = self.carbon_footprint_parser.parse_args()
        # Retrieve the carbon footprint record from the database by its ID
        footprint = CarbonFootPrintCountModel.query.get(footprint_id)
        if footprint:
            # If the footprint exists, update its attributes with the provided values
            footprint.user_id = args['user_id']
            footprint.carbon_value = args['carbon_value']
            footprint.date = args.get('date')
            # Commit the changes to the database
            db.session.commit()
            # Return a success message with status code 200
            return {'message': 'Carbon footprint count updated successfully'}, 200
        else:
            # If the footprint does not exist, return an error message with status code 404
            return {'error': 'Carbon footprint count not found'}, 404

    # Define a delete method to handle DELETE requests for deleting a specific footprint
    def delete(self, footprint_id):
        # Retrieve the carbon footprint record from the database by its ID
        footprint = CarbonFootPrintCountModel.query.get(footprint_id)
        if footprint:
            # If the footprint exists, delete it from the database
            db.session.delete(footprint)
            # Commit the changes to the database
            db.session.commit()
            # Return a success message with status code 200
            return {'message': 'Carbon footprint count deleted successfully'}, 200
        else:
            # If the footprint does not exist, return an error message with status code 404
            return {'error': 'Carbon footprint count not found'}, 404
