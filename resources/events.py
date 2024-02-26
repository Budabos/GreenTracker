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
          'image_url':event.image_url,
          'registration_deadline': event.registration_deadline.isoformat() if event.registration_deadline else None
      }

class EventsResource(Resource):
    # GET method to fetch all events
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
        # Retrieve all events from the database
        events = Events.query.all()

        # Serialize each event and return them along with a success status code
        serialized_events = [serialize_event(event) for event in events]

        return serialized_events, 200

    # POST method to create a new event
    def post(self):
        # Parse request data as JSON
        data = self.parser.parse_args()
         # Create a new event object
        new_event = Events(**data)
        
        # Add the new event to the database session and commit the transaction
        db.session.add(new_event)
        db.session.commit()
        
        # Serialize the new event and return it along with a success status code
        return {
          "message":"Event created successfully",
          "event":serialize_event(new_event)
        }, 201
    
class EventsResourceById(Resource):
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
        return {
          "message":"Event updated successfully",
          "event":serialize_event(event)
        }, 200


    # DELETE method to delete an existing event
    def delete(self, event_id):
        # Retrieve the event object from the database or return 404 if not found
        event = Events.query.get_or_404(event_id)
        
        # Delete the event from the database session and commit the transaction
        db.session.delete(event)
        db.session.commit()
        
        # Return empty response with success status code
        return {
          "message":"Event deleted successfully"
        }, 204
