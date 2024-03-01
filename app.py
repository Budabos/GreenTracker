from flask import Flask,session
# from flask_mail import Mail, Message
from resources.impact import ImpactMonitorings, ImpactMonitoringsById
from resources.carbon import CarbonFootprintCalculation, CarbonFootprintCalculationById, CalculationResourceByUser
from config import app, api
from resources.edu_resources import EduResource, EduResourceById
from resources.user import UserAccounts, SignUp, Login, UserById, ChangePassword, ForgotPassword, ResetPassword
from resources.events import EventsResource, EventsResourceById
from resources.partners import PartnerResource
from resources.feedback import Feedback
from resources.userEvent import User_Event
from resources.trackgoals import TrackGoalsResource
from resources.donations import DonationsResource, DonationsResourceById
from resources.review import ReviewsResource
from resources.products import ProductResource, ProductResourceById
from resources.summary import Summary
from resources.orders import Orders

# Add resources to the API
api.add_resource(EduResource, '/education-resources')
api.add_resource(EduResourceById, '/education-resources/<int:id>')
api.add_resource(UserAccounts, '/users')
api.add_resource(UserById, '/users/<int:id>')
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
api.add_resource(CalculationResourceByUser, '/carbon_calculations/<int:user_id>')

api.add_resource(DonationsResource, '/donations')
api.add_resource(DonationsResourceById,'/donations/<int:id>')
api.add_resource(ReviewsResource, '/reviews')
api.add_resource(Summary, '/summary')
api.add_resource(ChangePassword,'/change_password/<int:id>')
api.add_resource(Orders, '/orders')
api.add_resource(ForgotPassword, '/forgot-password')
api.add_resource(ResetPassword, '/reset')


if __name__ == '__main__':
    app.run(port=5555, debug=True)