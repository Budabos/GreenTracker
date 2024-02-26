from config import app, db
from models import Users

with app.app_context():
    Users.query.delete()
    db.session.commit()
    print("Successful users delete")