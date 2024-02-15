from flask import request
from flask_restful import Resource
from models import db, Events


class EventsResource(Resource):
    def get(self):
        events = Events.query.all()
        serialized_events = [self._serialize_event(event) for event in events]
        return serialized_events, 200

    def post(self):
        data = request.get_json()
        new_event = Events(**data)
        db.session.add(new_event)
        db.session.commit()
        return self._serialize_event(new_event), 201

    def patch(self, event_id):
        event = Events.query.get_or_404(event_id)
        data = request.get_json() or {}

        for field in ['title', 'description', 'location', 'date_event', 'organizer', 'contact_info', 'registration_deadline']:
            if field in data:
                setattr(event, field, data[field])

        db.session.commit()
        return self._serialize_event(event)

    def delete(self, event_id):
        event = Events.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return '', 204

    def _serialize_event(self, event):
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
