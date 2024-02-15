from config import app
from flask_restful import Api



api = Api(app)



from flask import Flask
from flask_restful import Api
from resources.impact import ImpactMonitorings
from resources.carbon import CarbonFootprintCalculation
from config import app, api
from resources.edu_resources import EduResource
from resources.user import UserAccounts
from resources.events import Events
from resources.partners import Partners
from resources.feedback import Feedback
from resources.userEvent import User_Event

# Add resources to the API
api.add_resource(EduResource, '/education-resources')
api.add_resource(UserAccounts, '/users')
api.add_resource(ImpactMonitorings, '/impact_monitorings')
api.add_resource(CarbonFootprintCalculation, '/calculate_footprint')
api.add_resource(Events, '/events')
api.add_resource(Partners, '/partners')
api.add_resource(Feedback, '/feedback', "/feedback/<int:id>")
api.add_resource(User_Event, '/event_user')

from flask_restful import Api

from resources.feedback import Feedback
from resources.userEvent import User_Event

api = Api(app)


api.add_resource(Feedback, '/feedback', "/feedback/<int:id>")
api.add_resource(User_Event, '/event_user')

from flask_restful import Api

from resources.feedback import Feedback
from resources.userEvent import User_Event

api = Api(app)


api.add_resource(Feedback, '/feedback', "/feedback/<int:id>")
api.add_resource(User_Event, '/event_user')


if __name__ == '__main__':
    app.run(port=5555, debug=True)