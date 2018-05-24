import unittest
import json
from app import create_app
import time


class TestApp(unittest.TestCase):
    def setUp(self):
        app = create_app('app.settings.Config')
        self.cli = app.test_client()

    def test_app(self):
        res = self.cli.get('/api/')
        self.assertEqual(200, res.status_code)

    def test_post_task(self):
        res = self.cli.post('/api/tasks', 
                       data=json.dumps({'task': 'my first task'}), 
                       content_type='application/json')
        self.assertEqual(200, res.status_code)

    def test_get_task(self):
        res = self.cli.get('/api/tasks')
        self.assertEqual(200, res.status_code)

    def test_async(self):
        req_url = 'http://google.com'
        res = self.cli.get(f'/api/async?url={req_url}')
        self.assertEqual(200, res.status_code)
        data = json.loads(res.data.decode('utf-8'), encoding='utf-8')
        task_id = data['task_id']

        result = None
        for _ in range(3):
            res = self.cli.get(f'/api/async/{task_id}')
            self.assertEqual(200, res.status_code)
            data = json.loads(res.data.decode('utf-8'), encoding='utf-8')
            if data['status'] == 'SUCCESS':
                result = data['result']
                break
            time.sleep(1)

        self.assertIn('google.com', result)

