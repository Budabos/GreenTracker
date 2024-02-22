from flask_restful import Resource, fields, reqparse 
from models import Donations, db
from datetime import datetime

# Define fields for serialization
donations_fields={
    "amount": fields.Integer,
    "date": fields.DateTime,
    "purpose": fields.String,
    "created_at": fields.DateTime,
}

class DonationsResource(Resource):
    # Define request parser for handling incoming data
    profile_parser = reqparse.RequestParser()
    
# Add expected arguments to the parser
    profile_parser.add_argument("amount", type=int, required=True, help="Amount is required")
    profile_parser.add_argument("date", type=datetime.fromisoformat, required=True, help="Date is required")
    profile_parser.add_argument("purpose", type=str, required=True, help="Purpose is required")

 # Handle POST requests
def post(self):
    # Parse request data
    data= DonationsResource.parser.parser_args()
    
    # Create a new donation object
    donation = Donations(**data)

    try:
        # Add and commit the donation to the database
        db.session.add(donation)
        db.session.commit()
        return {"message":"Donation created successfully"}
    except:
        # Return an error message if donation creation fails
        return {"message":"Donation not created"}
    
# Handle PATCH requests
def patch(self,id):
    # Parse request data
    data = DonationsResource.parser.parser_args

    # Retrieve the donation object from the database
    donation = Donations.query.get(id)

    # Update the donation object with the new data
    if donation:
        for key, value in data.items():
            setattr(donation, key, value)
        try:
             # Commit the changes to the database
            db.session.commit()
            return {"message":"Donation updated successfully"}
        except:
            # Return an error message if donation update fails
            return {"message":"Donation not updated"}

