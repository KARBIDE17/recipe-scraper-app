import os
from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

# Import Peewee models so tables can be created and used
from models.store import StoreModel
from models.item import ItemModel

# Import API blueprints
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

# Import the Peewee database instance
from database import db

# Factory function to create and configure the Flask app
def create_app():
    app = Flask(__name__)

    # Core Flask config settings
    app.config["PROPAGATE_EXCEPTIONS"] = True  # Ensures exceptions are visible in API responses (useful for debugging)

    # OpenAPI/Swagger documentation settings
    app.config["API_TITLE"] = "Store and Item API"            # Title for Swagger docs
    app.config["API_VERSION"] = "v1"                          # Version for the API
    app.config["OPENAPI_VERSION"] = "3.0.3"                   # OpenAPI version used
    app.config["OPENAPI_URL_PREFIX"] = "/"                   # Where Swagger UI is served
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"    # URL path for Swagger UI
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # External Swagger UI source


    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


    # Initialize the Flask-Smorest API manager
    api = Api(app)

    # Register your API blueprints (route collections)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    # Connect to the database and create necessary tables
    db.connect()
    db.create_tables([StoreModel, ItemModel])

    return app  # Return the Flask app instance
