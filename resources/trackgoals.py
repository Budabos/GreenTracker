from flask_restful import Resource, fields, marshal, reqparse 
from models import TrackGoals
from config import db
from datetime import datetime
from flask import request

# Define fields for marshalling track goals data
track_goals_fields={
    "user_id": fields.Integer,
    "id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
    "category": fields.String,
    "start_date": fields.DateTime,
    "end_date": fields.DateTime,
    "target_metric": fields.String,
    "target_value": fields.String,
    "current_value": fields.String,
    "status": fields.String,
    "note": fields.String,
    "reminder": fields.String,
    "created_at": fields.DateTime
}

class TrackGoalsResource(Resource):
    # Define request parser for handling incoming data
    profile_parser = reqparse.RequestParser()
    profile_parser.add_argument("title", type=str, required=True, help="Title is required")
    profile_parser.add_argument("user_id", type=int, required=True, help="Title is required")
    profile_parser.add_argument("description", type=str, required=True, help="Description is required")
    profile_parser.add_argument("category", type=str, required=True, help="Category is required")
    profile_parser.add_argument("start_date", type=str, required=True, help="Start date is required")
    profile_parser.add_argument("end_date",type=str, required=True, help="End date is required")
    profile_parser.add_argument("target_metric", type=str, required=True, help="Target metric is required")
    profile_parser.add_argument("target_value", type=str, required=True, help="Target value is required")
    profile_parser.add_argument("current_value", type=str, required=True, help="Current value is required")
    profile_parser.add_argument("status", type=str, required=True, help="Status is required")
    profile_parser.add_argument("note", type=str, required=True, help="Note is required")
    profile_parser.add_argument("reminder", type=str, required=True, help="Reminder is required")


    # GET method to fetch track goals by ID or all track goals
    def get(self, id=None):
        if id:
            # Fetch a specific track goal by ID
            track_goals = TrackGoals.query.filter_by(id=id).first()
            if track_goals:
                return marshal(track_goals, track_goals_fields), 200
            else:
                return {'message': 'No track goals found'}, 404
        else:
            # Fetch all track goals
            track_goals = TrackGoals.query.all()
            if track_goals:
                return marshal(track_goals, track_goals_fields), 200
            else:
                return {'message': 'No track goals found'}, 404

     # POST method to create a new track goal       
    def post(self):
        # Parse incoming data
        data= self.profile_parser.parse_args()

        # Create a new track goal object
        goal = TrackGoals(**data)

        try:
            # Add the new goal to the database
            db.session.add(goal)
            db.session.commit()
            return {"message":"Goal created successfully"},201
        except:
            return {"message":"Goal not created"},500

    # PATCH method to update an existing track goal
    def patch(self, id):
        # Parse incoming data
        data= TrackGoalsResource.parser_args()

    # Fetch the existing goal from the database
        goal = TrackGoals.query.get(id)

        if goal:
            # Update the goal attributes with new data
            for attr in request.json:
                setattr(goal, attr, request.json[attr])
            try:
                db.session.add(goal)       
                # Commit the changes to the database
                db.session.commit()
                return {"message":"Goal updated successfully", "goal":goal.to_dict()}, 200
            except:
                return {"message":"Goal not updated"},500

    # DELETE method to delete an existing track goal
    def delete(self, id):
        # Fetch the goal to be deleted from the database
        goal = TrackGoals.query.get(id)

        if goal:
            try:
                 # Delete the goal from the database
                db.session.delete(goal)
                db.session.commit()
                return {"message":"Goal deleted successfully"},204
            except:
                return {"message":"Goal not deleted"},500
        else:
            return {"message":"Goal not found"}, 404

