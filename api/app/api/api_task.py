from .bp import api_bp, custom_abort
from task.mytask import req_url

from flask import jsonify, request, abort, current_app
from celery.result import AsyncResult


@api_bp.route('/tasks', methods=['POST'])
def task_post():
    data = request.get_json(force=True)
    if 'task' not in data:
        custom_abort(400, 'task not in data', 'params/invalid')

    myapp = current_app
    db = myapp.extensions['pymongo']['MONGO'][1]
    doc_result = db.tasks.insert_one({
        'task': data['task']
    })

    if doc_result.acknowledged:
        return jsonify({'result': str(doc_result.inserted_id)})
    else:
        custom_abort(400, 'db insert error', 'db/insert')


@api_bp.route('/tasks', methods=['GET'])
def task_get():
    myapp = current_app
    db = myapp.extensions['pymongo']['MONGO'][1]

    docs = list(db.tasks.find({}, {'_id':0}))
    return jsonify({'result': docs})


@api_bp.route('/async', methods=['GET'])
def async_url():
    url = request.args.get('url')
    r = req_url.delay(url)
    return jsonify({'result': {'task_id': r.id}})


@api_bp.route('/async/<task_id>', methods=['GET'])
def async_get_task(task_id):
    res = AsyncResult(task_id)
    if res.successful():
        return jsonify({'result': {'status': res.status, 'result': res.result}})
    return jsonify({'result': {'status': res.status}})
