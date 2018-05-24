from flask import jsonify, request, abort, current_app
from app import core
from task.mytask import req_url
from celery.result import AsyncResult


@core.route('/tasks', methods=['POST'])
def task_post():
    data = request.get_json(force=True)
    if 'task' not in data:
        abort(400)

    myapp = current_app
    db = myapp.extensions['pymongo']['MONGO'][1]
    doc_result = db.tasks.insert_one({
        'task': data['task']
    })

    if doc_result.acknowledged:
        return jsonify({'data': 'ok'})
    else:
        abort(400)


@core.route('/tasks', methods=['GET'])
def task_get():
    myapp = current_app
    db = myapp.extensions['pymongo']['MONGO'][1]

    docs = list(db.tasks.find({}, {'_id':0}))
    return jsonify({'tasks': docs})


@core.route('/async', methods=['GET'])
def async_url():
    url = request.args.get('url')
    r = req_url.delay(url)
    return jsonify({'task_id': r.id})


@core.route('/async/<task_id>', methods=['GET'])
def async_get_task(task_id):
    res = AsyncResult(task_id)
    if res.successful():
        return jsonify({'status': res.status, 'result': res.result})
    return jsonify({'status': res.status})

