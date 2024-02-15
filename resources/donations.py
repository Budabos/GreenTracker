from flask_restful import Resource, fields, reqparse 
from models import Donations
from config import db
from datetime import datetime
from flask import request


donations_fields={
    "amount": fields.Integer,
    "date": fields.DateTime,
    "purpose": fields.String,
    "created_at": fields.DateTime,
}

class DonationsResource(Resource):
    profile_parser = reqparse.RequestParser()

    profile_parser.add_argument("amount", type=str, required=True, help="Amount is required")
    profile_parser.add_argument("date", type=str, required=True, help="Date is required")
    profile_parser.add_argument("purpose", type=str, required=True, help="Purpose is required")
    profile_parser.add_argument("user_id", type=int, required=True, help="Purpose is required")
    
    def get(self):
        donations = [donation.to_dict() for donation in Donations.query.all()]
        
        return donations, 200

    def post(self):
        data= self.profile_parser.parse_args()
        
        # donations the model
        donation = Donations(**data)

        try:
            db.session.add(donation)
            db.session.commit()
            return {"message":"Donation created successfully"}
        except:
            return {"message":"Donation not created"}
        

class DonationsResourceById(Resource):
    def patch(self,id):
        donation = Donations.query.get(id)

        if donation:
            for attr in request.json:
                setattr(donation, attr, request.json[attr])
            try:
                db.session.add(donation)
                db.session.commit()
                return {"message":"Donation updated successfully", "donation":donation.to_dict()}
            except:
                return {"message":"Donation not updated"}

