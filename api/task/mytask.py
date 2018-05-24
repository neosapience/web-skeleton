from task import celery_app
import requests


class FailHandlingTask(celery_app.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f'on_failure: {args[0]}')


def _req_url(address):
    res = requests.get(address)
    if res.status_code != 200:
        return False
    return res.url


@celery_app.task(base=FailHandlingTask)
def req_url(address):
    res = _req_url(address)
    if not res:
        raise RuntimeError('error: req_url')
    return res
