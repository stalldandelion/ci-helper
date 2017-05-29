from flask import url_for, jsonify, abort
from lib.nexus_class import NexusHelperClass


def make_public_task(task):

    new_task = {}
    for field in task:
        if field == 'function_parameter':
            if task['function_parameter']:
                new_task['uri'] = url_for('perform_task_id', task_id=task['id'],
                                          param=task['function_parameter'], url=task['function_url'],
                                          _external=True)
            else:
                new_task['uri'] = url_for('perform_task_id', task_id=task['id'],
                                          url=task['function_url'], _external=True)
                # new_task['uri'] = url_for('perform_task_id', task_id=task['id'], _external=True)
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


def getleverables(url='sadbprodnexus9.sfa.se:8081'):
    nexushelper = NexusHelperClass(url)
    return nexushelper.get_leverables()


def getartefacts(leverable, url='sadbprodnexus9.sfa.se:8081'):
    nexushelper = NexusHelperClass(url)
    return nexushelper.get_artefacts(leverable)


def getartefactversions(artefact, url='sadbprodnexus9.sfa.se:8081'):
    nexushelper = NexusHelperClass(url)
    return nexushelper.get_artefactversions(artefact)

