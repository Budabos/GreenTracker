from config import app, api
from resources.edu_resources import EduResource

api.add_resource(EduResource, '/education-resources')

if __name__ == '__main__':
    app.run(port=5555, debug=True)