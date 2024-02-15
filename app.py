from config import app
from flask import Flask
from flask_restful import Api
from resources import ImpactMonitorings, CarbonFootprintCalculation


# Create Flask app instance
app = Flask(__name__)

# Initialize Flask-Restful API
api = Api(app)

# Add resources to the API
api.add_resource(ImpactMonitorings, '/impact_monitorings')
api.add_resource(CarbonFootprintCalculation, '/calculate_footprint')








if __name__ == '__main__':
    app.run(port=5555, debug=True)