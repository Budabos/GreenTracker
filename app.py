from flask import Flask
from flask_restful import Api
from resources.impact import ImpactMonitorings
from resources.carbon import CarbonFootprintCalculation
from config import app, api
from resources.edu_resources import EduResource
from resources.user import UserAccounts, SignUp, Login
from resources.events import Events
from resources.partners import Partners

# Add resources to the API
api.add_resource(EduResource, '/education-resources')
api.add_resource(UserAccounts, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(ImpactMonitorings, '/impact_monitorings')
api.add_resource(CarbonFootprintCalculation, '/calculate_footprint')
# api.add_resource(Events, '/events')
# api.add_resource(Partners, '/partners')


if __name__ == '__main__':
    app.run(port=5555, debug=True)