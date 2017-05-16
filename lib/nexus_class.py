class NexusHelperClass:
    """A class of nexus functions"""
    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_repos():
        """
        Gets all repos from nexus
        :return: list
        """

        repos = []

        return repos

    @staticmethod
    def get_leverables():
        """
        Gets all groups (leverables) from nexus
        :return: list
        """

        leverables = []

        return leverables

    @staticmethod
    def get_artefacts(leverables):
        """
        Gets all artefacts from all leverables in nexus
        
        :param leverables: 
        :type leverables list
        :return: dict
        """

        for lev in leverables:
            print(lev)

        artefacts = {}

        return artefacts

    @staticmethod
    def get_artefactversions(artefacts):
        """
        Gets all artefact version from artefacts
        
        :param artefacts:
        :type artefacts dict
        :return: dict of dicts 
        """
        for artefact in artefacts:
            print(artefact)

        artefactversions = {}

        return artefactversions
