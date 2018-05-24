from flask import Blueprint, jsonify
core = Blueprint('core', __name__)


@core.route('/')
def index():
    return jsonify({'data': 'ok'})

