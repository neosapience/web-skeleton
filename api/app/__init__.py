from flask import Flask, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo
from app.core import core
from app import api_task


def create_app(object_name):
    myapp = Flask(__name__)
    myapp.config.from_object(object_name)
    CORS(myapp)
    PyMongo(myapp)

    # initialize the cache
    # cache.init_app(app)
    # initialize the debug tool bar
    # debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    # db.init_app(app)

    # login_manager.init_app(app)

    # Import and register the different asset bundles
    # assets_env.init_app(app)
    # assets_loader = PythonAssetsLoader(assets)
    # for name, bundle in assets_loader.load_bundles().items():
    #     assets_env.register(name, bundle)

    @myapp.errorhandler(400)
    def custom400(error):
        return make_response(jsonify({'error': error.description}), 400)

    # register our blueprints
    myapp.register_blueprint(core, url_prefix='/api')
    return myapp
