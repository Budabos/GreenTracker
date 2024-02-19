from flask import request
from flask_restful import Resource, reqparse
from models import db, Events

def serialize_event(event):
      return {
          'id': event.id,
          'title': event.title,
          'description': event.description,
          'location': event.location,
          'date_event': event.date_event.isoformat(),
          'organizer': event.organizer,
          'contact_info': event.contact_info,
          'registration_deadline': event.registration_deadline.isoformat() if event.registration_deadline else None
      }

class EventsResource(Resource):
    parser = reqparse.RequestParser()
        
    parser.add_argument('title', type=str, required=True, help='Title is required')
    parser.add_argument('description', type=str, required=True, help='Description is required')
    parser.add_argument('location', type=str, required=True, help='Location is required')
    parser.add_argument('image_url', type=str, required=True, help='Image url is required')
    parser.add_argument('date_event', required=True, help='Content is required')
    parser.add_argument('organizer', type=str, required=True, help='Author is required')
    parser.add_argument('contact_info', type=str, required=True, help='Contact info is required')
    parser.add_argument('registration_deadline', required=True, help='Registration deadline is required')
        
    def get(self):
        events = Events.query.all()
        serialized_events = [serialize_event(event) for event in events]
        return serialized_events, 200

    def post(self):
        data = self.parser.parse_args()
        new_event = Events(**data)
        db.session.add(new_event)
        db.session.commit()
        return serialize_event(new_event), 201
    
class EventsResourceById(Resource):
    def patch(self, event_id):
        event = Events.query.get_or_404(event_id)
        data = request.get_json() or {}

        for field in ['title', 'description', 'location', 'date_event', 'organizer', 'contact_info', 'registration_deadline']:
            if field in data:
                setattr(event, field, data[field])

        db.session.commit()
        return serialize_event(event)

    def delete(self, event_id):
        event = Events.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return '', 204

  
