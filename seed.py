from config import app, db
from models import FeedbackForm

with app.app_context():
    FeedbackForm.query.delete()
    db.session.commit()
    print("Successful feedback delete")