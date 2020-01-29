import json
from app import create_app
import time
import os


def test_health():
    app = create_app('app_settings.ConfigDebug')
    cli = app.test_client()
    r = cli.get('/api/health')
    assert 200 == r.status_code


def test_version():
    app = create_app('app_settings.ConfigDebug')
    cli = app.test_client()
    r = cli.get('/api/v')
    assert 200 == r.status_code
    assert os.environ['MYAPP_API_VERSION'] == r.get_json()['result']


def test_post_task():
    app = create_app('app_settings.ConfigDebug')
    cli = app.test_client()
    r = cli.post(
        '/api/tasks',
        data=json.dumps({'task': 'my first task'}), 
        content_type='application/json')
    assert 200 == r.status_code
    assert 'result' in r.get_json()


def test_get_task():
    app = create_app('app_settings.ConfigDebug')
    cli = app.test_client()
    r = cli.get('/api/tasks')
    assert 200 == r.status_code
    assert 'result' in r.get_json()


def test_async():
    app = create_app('app_settings.ConfigDebug')
    cli = app.test_client()
    req_url = 'http://google.com'
    r = cli.get(f'/api/async?url={req_url}')
    assert 200 == r.status_code
    data = r.get_json()['result']
    task_id = data['task_id']

    result = None
    for _ in range(3):
        r = cli.get(f'/api/async/{task_id}')
        assert 200 == r.status_code
        data = r.get_json()['result']
        if data['status'] == 'SUCCESS':
            result = data['result']
            break
        time.sleep(1)

    assert 'google.com' in result
