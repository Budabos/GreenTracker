from config import app, db
from models import Users

with app.app_context():
    found_user = Users.query.filter(Users.phone == '0734567812').filter(Users.id != 20).first()
    print(found_user)