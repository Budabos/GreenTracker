from flask_restful import Resource, fields, reqparse 
from models import Donations, db
from datetime import datetime


donations_fields={
    "amount": fields.Integer,
    "date": fields.DateTime,
    "purpose": fields.String,
    "created_at": fields.DateTime,
}

class DonationsResource(Resource):
    profile_parser = reqparse.RequestParser()

    profile_parser.add_argument("amount", type=int, required=True, help="Amount is required")
    profile_parser.add_argument("date", type=datetime.fromisoformat, required=True, help="Date is required")
    profile_parser.add_argument("purpose", type=str, required=True, help="Purpose is required")

def post(self):
    data= DonationsResource.parser.parser_args()
    
    # donations the model
    donation = Donations(**data)

    try:
        db.session.add(donation)
        db.session.commit()
        return {"message":"Donation created successfully"}
    except:
        return {"message":"Donation not created"}
    

def patch(self,id):
    data = DonationsResource.parser.parser_args

    donation = Donations.query.get(id)

    if donation:
        for key, value in data.items():
            setattr(donation, key, value)
        try:
            db.session.commit()
            return {"message":"Donation updated successfully"}
        except:
            return {"message":"Donation not updated"}

