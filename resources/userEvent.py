from flask_restful import Resource,abort,fields,marshal_with
from models import UserEvents
from config import db

resource_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'event_id': fields.String,
    'date': fields.DateTime
}

class User_Event(Resource):
    #get list of all the events the user has particiated
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
        