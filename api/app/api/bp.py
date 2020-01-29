from flask import Blueprint, jsonify, abort, current_app
api_bp = Blueprint('api', __name__)


def custom_abort(status_code, msg, error_code=''):
    current_app.logger.error(f'[{error_code}]: {msg}')
    abort(status_code, description={'msg': msg, 'error_code': error_code})
