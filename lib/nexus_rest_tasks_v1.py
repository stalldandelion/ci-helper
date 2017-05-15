tasks = [
    {
        'id': 'getleverables',
        'title': u'Leverables',
        'description': u'Get all leverables in nexus rpm-repo',
        'functioncall': u'getleverables',
        'done': False
    },

    {
        'id': 'getartefacts',
        'title': u'Artefacts',
        'description': u'Get all arefacts from a leverable',
        'functioncall': u'getartefacts?leverable',
        'function_parameter': u'leverable',
        'done': False
    },

    {
        'id': 'getartefactversions',
        'title': u'Aretefact versions',
        'description': u'Get all versions of an artefact',
        'functioncall': u'getartefactversions',
        'function_parameter': u'artefact',
        'done': False
    },

    {
        'id': 'getall',
        'title': u'All artefacts and versions',
        'description': u'Get all arefacts and versions in nexus',
        'functioncall': u'getall',
        'done': False
    }
]
