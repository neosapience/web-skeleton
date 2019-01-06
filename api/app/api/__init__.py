from .bp import api_bp
from . import api_task
from flask import jsonify


@api_bp.route('/')
def index():
    return jsonify({'result': 'ok'})
