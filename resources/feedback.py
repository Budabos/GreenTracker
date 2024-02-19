from flask_restful import Resource,reqparse,abort,fields,marshal_with
from models import FeedbackForm
from config import db

resource_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'feedback_text': fields.String,
    'feedback_type': fields.String,
    'date': fields.DateTime
}

class Feedback(Resource):
    #user fills a form(post)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='name is required', required=True)
        parser.add_argument('email', type=str, help='email is required', required=True)
        parser.add_argument('feedback_message', type=str, help='feedback_message is required', required=True)
        args = parser.parse_args()
        
        feedback = FeedbackForm(**args)

        try:
            db.session.add(feedback)
            db.session.commit()
            return {"message":"Form created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def get(self, id=None):
        if id:
            feedback = FeedbackForm.query.filter(FeedbackForm.id == id).first()
            
            if not feedback:
                return {"message":"Feedback not found"},404

            return feedback
        else:
            feedback = [feed.to_dict() for feed in FeedbackForm.query.all()]

            return feedback
