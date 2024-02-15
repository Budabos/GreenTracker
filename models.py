from config import db
from sqlalchemy_serializer import SerializerMixin

class Education_Resources(db.Model, SerializerMixin):
    __tablename__ = 'educational_resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    date_published = db.Column(db.DateTime, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Reviews(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id= db.Column(db.Integer, db.ForeignKey("products.id"))
    rating = db.Column(db.String, nullable=False)
    review_text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, server_default=db.func.now())
    
    
class Users(db.Model):
    __tablename__ ="users"
    
    id= db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    
    phone=db.Column(db.Integer, nullable=False)
    password=db.Column(db.String, nullable=False)
    gender=db.Column(db.String, nullable=False)
    
    status=db.Column(db.String, nullable=False)
    last_login = db.Column(db.String)
    
    role = db.Column(db.String, nullable=False)
    interests = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Events(db.Model):
    __tablename__ = 'events'
    
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    date_event = db.Column(db.DateTime, nullable=False)
    organizer = db.Column(db.String, nullable=False)
    contact_info = db.Column(db.String, nullable=False)
    registration_deadline = db.Column(db.DateTime, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Products(db.Model):
    __tablename__ ="products"
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    category=db.Column(db.String, nullable=False)
    brand=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    eco_rating=db.Column(db.String, nullable=False)
    manufacturer_link=db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Donations(db.Model):
    __tablename__ ="donations"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    amount=db.Column(db.String, nullable=False)
    date=db.Column(db.DateTime, nullable=False)
    purpose=db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Partners(db.Model):
    __tablename__ ="partners"
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    contact_info=db.Column(db.String, nullable=False)
    website=db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class CarbonFootPrintCount(db.Model):
    __tablename__ ="carbon_footprint_counts"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    carbon_value=db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())

class Impact_Monitorings(db.Model):
    __tablename__ ="impact_monitorings"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    
    action_taken = db.Column(db.String, nullable=False)
    carbon_footprint = db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class TrackGoals(db.Model):
    __tablename__ ="track_goals"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    title=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    category=db.Column(db.String, nullable=False)
    start_date=db.Column(db.DateTime, nullable=False)
    end_date=db.Column(db.DateTime, nullable=False)
    target_metric=db.Column(db.String, nullable=False)
    target_value=db.Column(db.String, nullable=False)
    current_value=db.Column(db.String, nullable=False)
    status=db.Column(db.String, nullable=False)
    note=db.Column(db.String, nullable=False)
    reminder=db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class UserEvents(db.Model):
    __tablename__ ="user_events"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id= db.Column(db.Integer, db.ForeignKey("events.id"))
    
    date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    
class FeedbackForm(db.Model):
    __tablename__ ="feedback_forms"
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"))
    feedback_text = db.Column(db.String, nullable=False) 
    feedback_type = db.Column(db.String, nullable=False) 
    date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)