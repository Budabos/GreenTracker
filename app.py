from config import app, api, bcrypt
from resources.edu_resources import EduResource
from resources.user import UserAccounts
from models import Users

api.add_resource(EduResource, '/education-resources')
api.add_resource(UserAccounts, '/users')

if __name__ == '__main__':
    app.run(port=5555, debug=True)