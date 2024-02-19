from config import app, db
from models import Education_Resources, Events

with app.app_context():
    Events.query.delete()
    db.session.commit()
    print("Successful feedback delete")