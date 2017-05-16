from flask import Flask, jsonify, make_response, request
from lib.nexus_rest_tasks_v1 import tasks as v1tasks
from lib.nexus_rest_functions import get_tasks, get_task


app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/ci-helper/rest/v1/tasks', methods=['GET'])
def show_tasks():

    return get_tasks(v1tasks)


@app.route('/ci-helper/rest/v1/tasks/<string:task_id>', methods=['GET'])
def show_task_id(task_id):

    if request.args:
        print(request.args['param'])
        return 'misu'
    else:
        return get_task(v1tasks, task_id)


if __name__ == '__main__':
    app.run(host='localhost',
            port=25003,
            debug=True)