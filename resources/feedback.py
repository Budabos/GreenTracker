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
    parser = reqparse.RequestParser()
    parser.add_argument('feedback_text', type=str, help='feedback_text is required', required=True)
    parser.add_argument('feedback_type', type=str, help='feedback_type is required', required=True)
    args = parser.parse_args()

    #user fills a form(post)
    def post(self):
        data = Feedback.parser.parse_args()
        feedback = FeedbackForm(**data)

        try:
            db.session.add(feedback)
            db.session.commit()
            return {"message":"Form created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    @marshal_with(resource_fields)
    def get(self, id=None):
        if id:
            feedback = FeedbackForm.query.get(id)

            return feedback
        else:
            feedback = FeedbackForm.query.all()

            return feedback
