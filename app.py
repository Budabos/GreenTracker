from config import app
from flask_restful import Api

from resources.feedback import Feedback
from resources.userEvent import User_Event

api = Api(app)


api.add_resource(Feedback, '/feedback', "/feedback/<int:id>")
api.add_resource(User_Event, '/event_user')


if __name__ == '__main__':
    app.run(port=5555, debug=True)