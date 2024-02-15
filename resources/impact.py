# Import necessary modules
from flask_restful import Resource, reqparse, fields
from models import db, Impact_Monitorings

# This dictionary defines the fields associated with an Impact_Monitorings resource.
Impact_Monitorings_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "action_taken": fields.String,
    "carbon_footprint": fields.String,
    "created_at": fields.String
}

# Define a class named ImpactMonitorings that inherits from Resource
class ImpactMonitorings(Resource):
    # Define a parser to parse incoming request data for ImpactMonitorings
    impact_monitorings_parser = reqparse.RequestParser()
    impact_monitorings_parser.add_argument("user_id", type=int, required=True, help="User ID is required")
    impact_monitorings_parser.add_argument("action_taken", type=str, required=True, help="Action taken is required")
    impact_monitorings_parser.add_argument("carbon_footprint", type=str, required=True, help="Carbon footprint is required")

    # POST method to handle creating new ImpactMonitorings instances
    def post(self):
        # Parse the arguments from the request
        args = self.impact_monitorings_parser.parse_args()

        # Create a new instance of Impact_MonitoringsModel with parsed arguments
        new_impact_monitoring = Impact_Monitorings(
            user_id=args["user_id"],
            action_taken=args["action_taken"],
            carbon_footprint=args["carbon_footprint"],
        )

        try:
            # Add the new instance to the database session
            db.session.add(new_impact_monitoring)
            
            # Commit the changes to the database
            db.session.commit()

            # Return a success message and status code 201
            return {'message': 'Impact monitoring record created successfully'}, 201
        except Exception as e:
            # If there's an error, rollback changes and return an error message with status code 500
            db.session.rollback()
            return {'error': 'An error occurred while creating impact monitoring record'}, 500




   # GET method to retrieve an ImpactMonitorings instance by ID
def get(self, id):
    # Query the database for the ImpactMonitorings instance with the specified ID
    impact_monitoring = Impact_MonitoringsModel.query.get(id)
    
    if impact_monitoring:
        # If the instance is found, return its data and status code 200
        return impact_monitoring.serialize(), 200
    else:
        # If the instance is not found, return an error message and status code 404
        return {'error': 'Impact monitoring record not found'}, 404

# PUT method to update an existing ImpactMonitorings instance
def put(self, id):
    # Parse the arguments from the request
    args = self.impact_monitorings_parser.parse_args()
    
    # Query the database for the ImpactMonitorings instance with the specified ID
    impact_monitoring = Impact_MonitoringsModel.query.get(id)

    if impact_monitoring:
        # If the instance is found, update its attributes with the parsed arguments
        impact_monitoring.user_id = args["user_id"]
        impact_monitoring.action_taken = args["action_taken"]
        impact_monitoring.carbon_footprint = args["carbon_footprint"]
        impact_monitoring.created_at = args["created_at"]

        try:
            # Commit the changes to the database
            db.session.commit()

            # Return a success message and status code 200
            return {'message': 'Impact monitoring record updated successfully'}, 200
        except Exception as e:
            # If there's an error, rollback changes and return an error message with status code 500
            db.session.rollback()
            return {'error': 'An error occurred while updating impact monitoring record'}, 500
    else:
        # If the instance is not found, return an error message and status code 404
        return {'error': 'Impact monitoring record not found'}, 404

# DELETE method to delete an existing ImpactMonitorings instance
def delete(self, id):
    # Query the database for the ImpactMonitorings instance with the specified ID
    impact_monitoring = Impact_MonitoringsModel.query.get(id)
    
    if impact_monitoring:
        # If the instance is found, delete it from the database
        db.session.delete(impact_monitoring)

        try:
            # Commit the changes to the database
            db.session.commit()

            # Return a success message and status code 200
            return {'message': 'Impact monitoring record deleted successfully'}, 200
        except Exception as e:
            # If there's an error, rollback changes and return an error message with status code 500
            db.session.rollback()
            return {'error': 'An error occurred while deleting impact monitoring record'}, 500
    else:
        # If the instance is not found, return an error message and status code 404
        return {'error': 'Impact monitoring record not found'}, 404
