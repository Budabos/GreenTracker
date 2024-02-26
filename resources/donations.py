from flask_restful import Resource, fields, reqparse 
from models import Donations
from config import db
from datetime import datetime
from flask import request

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
    profile_parser.add_argument("date", required=True, help="Date is required")
    profile_parser.add_argument("purpose", type=str, required=True, help="Purpose is required")
    profile_parser.add_argument("user_id", type=int, required=True, help="User ID is required")
    
    def get(self):
        #Loop over donations in db
        donations = [donation.to_dict() for donation in Donations.query.all()]
        
        #Return all found donations
        return donations, 200

    # Handle POST requests
    def post(self):
        # Parse request data
        data= self.profile_parser.parse_args()

        # Create a new donation object
        donation = Donations(**data)

        try:
            # Add and commit the donation to the database
            db.session.add(donation)
            db.session.commit()
            return {"message":"Donation created successfully"}
        except:
            # Return an error message if donation creation fails
            return {"message" : "Donation creation failed"}
           
class DonationsResourceById(Resource):
    def patch(self,id):
        #Find donation by id
        donation = Donations.query.get(id)

        #Loop over the request object and change the desired attributes
        if donation:
            for attr in request.json:
                setattr(donation, attr, request.json[attr])
            try:
                #Add to the db
                db.session.add(donation)
                #Commit changes to db
                db.session.commit()
                return {"message":"Donation updated successfully", "donation":donation.to_dict()}
            except:
                return {"message":"Donation not updated"}
        else:
          return {
            "message":"Donation not found"
          },404

