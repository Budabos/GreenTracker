from flask_jwt_extended import jwt_required
from flask_restful import Resource,abort,fields,marshal_with, reqparse
from models import Events, UserEvents
from config import db

resource_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'event_id': fields.String,
    'date': fields.DateTime
}

class User_Event(Resource):
    #get list of all the events the user has particiated
    @jwt_required()
    @marshal_with(resource_fields)
    def get(self, id=None):
        if id:
            event = UserEvents.query.get(id)
            if not event:
                abort(404,message='Event not found')

            return event
        else:
            events = UserEvents.query.all()

            return events
        
    @jwt_required()    
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument('user_id', type=int, required=True, help='User ID is required')
        parser.add_argument('event_id', type=int, required=True, help='Event ID is required')
        
        args = parser.parse_args()
        
        new_user_event = UserEvents(**args)
        found_event = Events.query.filter(Events.id == args['event_id']).first()
        
        db.session.add(new_user_event)
        db.session.commit()
        
        return {
            "message":"Booking successful",
            "user_event":new_user_event.to_dict(),
        },201
        