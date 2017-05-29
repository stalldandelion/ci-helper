from flask import Flask, make_response, request
from lib.nexus_rest_tasks_v1 import tasks as v1tasks
from lib.nexus_rest_functions import *

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


@app.route('/')
@app.route('/ci-helper/rest/v1/tasks', methods=['GET'])
def show_tasks():

    return get_tasks(v1tasks)


@app.route('/ci-helper/rest/v1/tasks/<string:task_id>', methods=['GET'])
def perform_task_id(task_id):

    if request.args:
        if 'param' in request.args:
            if 'url' in request.args:
                try:
                    return jsonify({request.args['param']: globals()[task_id](request.args['param'],
                                                                              request.args['url'])})
                except:
                    abort(400)
            else:
                try:
                    return jsonify({request.args['param']: globals()[task_id](request.args['param'])})
                except:
                    abort(400)
        elif 'url' in request.args:
            return jsonify(globals()[task_id](request.args['url']))
        else:
            if request.args:
                abort(400)
            else:
                abort(404)
    else:
        if [x for x in v1tasks if x['id'] == task_id]:
            return 'Error. Url and or param missing'
        else:
            abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=25003,
            debug=True)
