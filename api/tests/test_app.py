import unittest
import json
from app import create_app
import time


class TestApp(unittest.TestCase):
    def setUp(self):
        app = create_app('app_settings.ConfigDebug')
        self.cli = app.test_client()

    def test_app(self):
        r = self.cli.get('/api/health')
        self.assertEqual(200, r.status_code)

    def test_post_task(self):
        r = self.cli.post('/api/tasks', 
                       data=json.dumps({'task': 'my first task'}), 
                       content_type='application/json')
        self.assertEqual(200, r.status_code)
        self.assertIn('result', r.get_json())

    def test_get_task(self):
        r = self.cli.get('/api/tasks')
        self.assertEqual(200, r.status_code)
        self.assertIn('result', r.get_json())

    def test_async(self):
        req_url = 'http://google.com'
        r = self.cli.get(f'/api/async?url={req_url}')
        self.assertEqual(200, r.status_code)
        data = r.get_json()['result']
        task_id = data['task_id']

        result = None
        for _ in range(3):
            r = self.cli.get(f'/api/async/{task_id}')
            self.assertEqual(200, r.status_code)
            data = r.get_json()['result']
            if data['status'] == 'SUCCESS':
                result = data['result']
                break
            time.sleep(1)

        self.assertIn('google.com', result)

