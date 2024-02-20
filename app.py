from flask import Flask
from resources.impact import ImpactMonitorings, ImpactMonitoringsById
from resources.carbon import CarbonFootprintCalculation, CarbonFootprintCalculationById
from config import app, api
from resources.edu_resources import EduResource
from resources.user import UserAccounts, SignUp, Login
from resources.events import EventsResource, EventsResourceById
from resources.partners import PartnerResource
from resources.feedback import Feedback
from resources.userEvent import User_Event
from resources.trackgoals import TrackGoalsResource
from resources.donations import DonationsResource, DonationsResourceById
from resources.review import   Reviews
from resources.products import ProductResource, ProductResourceById


# Add resources to the API
api.add_resource(EduResource, '/education-resources')
api.add_resource(UserAccounts, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
api.add_resource(ImpactMonitorings, '/impact_monitorings')
api.add_resource(ImpactMonitoringsById, '/impact_monitorings/<int:id>')
api.add_resource(CarbonFootprintCalculation, '/calculate_footprint')
api.add_resource(CarbonFootprintCalculationById, '/calculate_footprint/<int:footprint_id>')
api.add_resource(EventsResource, '/events')
api.add_resource(EventsResourceById, '/events/<int:event_id>')
api.add_resource(PartnerResource, '/partners')
api.add_resource(Feedback, '/feedback', "/feedback/<int:id>")
api.add_resource(User_Event, '/event_user')
api.add_resource(TrackGoalsResource, '/track_goals','/track_goals/<int:id>')
api.add_resource(ProductResource, '/products')
api.add_resource(ProductResourceById, '/products/<int:id>')


api.add_resource(DonationsResource, '/donations')
api.add_resource(DonationsResourceById,'/donations/<int:id>')
#api.add_resource(Reviews, '/review')


if __name__ == '__main__':
    app.run(port=5555, debug=True)