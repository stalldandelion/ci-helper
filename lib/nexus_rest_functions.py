from flask import url_for, jsonify, abort
from lib.nexus_class import NexusHelperClass


def make_public_task(task):

    new_task = {}
    for field in task:
        if field == 'functioncall':
            if 'function_parameter' in task:
                new_task['uri'] = url_for('show_task_id', task_id=task['id'], param=task['function_parameter'],
                                          _external=True)
            else:
                new_task['uri'] = url_for('show_task_id', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


def get_tasks(tasks):

    return jsonify({'tasks': [make_public_task(task) for task in tasks]})


def get_task(tasks, task_id):

    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)

    return jsonify({'task': task[0]})


def getleverables(intext):
    nexushelper = NexusHelperClass('url')
    print(nexushelper.get_leverables())


def getartefacts(intext):
    nexushelper = NexusHelperClass('url')
    print(nexushelper.get_leverables())


def getartefactversions(intext):
    nexushelper = NexusHelperClass('url')
    print(nexushelper.get_leverables())