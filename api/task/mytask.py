from . import celery_app
import requests


class FailHandlingTask(celery_app.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f'on_failure: {args[0]}')


def _req_url(address):
    r = requests.get(address)
    if r.status_code != 200:
        return False
    return r.url


@celery_app.task(base=FailHandlingTask)
def req_url(address):
    r = _req_url(address)
    if not r:
        raise RuntimeError('error: req_url')
    return r
