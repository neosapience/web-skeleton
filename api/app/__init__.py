from app.api import api_bp
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo


def extension_mongo(flask_app):
    mongo = PyMongo(flask_app)
    if 'pymongo' not in flask_app.extensions.keys():
        flask_app.extensions['pymongo'] = {
            'MONGO': (mongo.cx, mongo.db,)
        }


def create_app(object_name):
    myapp = Flask(__name__)
    myapp.config.from_object(object_name)
    CORS(myapp)
    extension_mongo(myapp)

    @myapp.errorhandler(400)
    def custom400(error):
        return make_response(jsonify({'error': error.description}), 400)

    # register our blueprints
    myapp.register_blueprint(api_bp, url_prefix='/api')
    return myapp
