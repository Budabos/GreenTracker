from flask import request
from flask_restful import Resource
from models import db, Events

class EventsResource(Resource):
    
    # GET method to fetch all events
    def get(self):
        # Retrieve all events from the database
        events = Events.query.all()
        # Serialize each event and return them along with a success status code
        serialized_events = [self._serialize_event(event) for event in events]
        return serialized_events, 200

    # POST method to create a new event
    def post(self):
        # Parse request data as JSON
        data = request.get_json()
        
        # Create a new event object
        new_event = Events(**data)
        
        # Add the new event to the database session and commit the transaction
        db.session.add(new_event)
        db.session.commit()
        
        # Serialize the new event and return it along with a success status code
        return self._serialize_event(new_event), 201

    # PATCH method to update an existing event
    def patch(self, event_id):
        # Retrieve the event object from the database or return 404 if not found
        
        event = Events.query.get_or_404(event_id)
        # Parse request data as JSON or create an empty dictionary if no data is provided
        data = request.get_json() or {}

        # Update fields of the event with provided data
        for field in ['title', 'description', 'location', 'date_event', 'organizer', 'contact_info', 'registration_deadline']:
            if field in data:
                setattr(event, field, data[field])
                
        # Commit the changes to the database
        db.session.commit()
        # Serialize the updated event and return it
        return self._serialize_event(event)

    # DELETE method to delete an existing event
    def delete(self, event_id):
        # Retrieve the event object from the database or return 404 if not found
        event = Events.query.get_or_404(event_id)
        
        # Delete the event from the database session and commit the transaction
        db.session.delete(event)
        db.session.commit()
        # Return empty response with success status code
        return '', 204

    # Helper method to serialize event object
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
