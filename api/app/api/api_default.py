from .bp import api_bp
from flask import jsonify
import os


@api_bp.route('/health')
def health():
    return jsonify({'result': 'ok'})


@api_bp.route('/v')
def version():
    return jsonify({'result': os.environ['MYAPP_API_VERSION']})
