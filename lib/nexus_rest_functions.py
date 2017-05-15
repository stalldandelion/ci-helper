from flask import url_for, jsonify, abort
from lib.nexus_class import NexusHelperClass

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('ci-helper/rest/v1/tasks', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


def get_tasks(tasks):

    return jsonify({'tasks': tasks})


def get_task(tasks, task_id):
    task = [task for task in tasks if task['id'] == task_id]

    # print(task[0]['title'])
    # functioncall = eval(task[0]['functioncall'])
    # functioncall('test')
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