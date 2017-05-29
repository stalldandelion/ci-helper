from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import logging
import xml.etree.ElementTree as elementTree
logger = logging.getLogger(__name__)


class NexusHelperClass:
    """ A class of nexus functions
        Url is a string of host:port"""

    def __init__(self, url):
        self.url = url

    # @staticmethod
    def get_repos(self):
        """ Gets all repos from nexus"""

        if self.url == 'test':
            repos = ['feature', 'dev', 'int']
        else:
            repos = []

        return repos

    # @staticmethod
    def get_leverables(self):
        """ Get all leverables from nexus"""
        import re

        """
        Gets all groups (leverables) from nexus
        :return: list
        """
        if self.url == 'test':
            leverabellist = ['asu', 'bll', 'tfp']
        else:
            leverabellist = []
            try:
                response = urlopen('http://' + self.url + '/nexus/content/repositories/rpm-dev/fk/rpm/')
            except (HTTPError, URLError) as e:
                logger.error(e)
                return ['Error getting leverables!!!']

            for rline in response:
                line = rline.decode("utf-8")
                if re.match(".*<td>(.*)/repositories/(.*)", line):
                    leverabellist.append(line.split('">')[-1].split('/')[0])

        return leverabellist

    # @staticmethod
    def get_artefacts(self, leverable):
        """
        Gets all artefacts from all leverables in nexus
        
        :param leverable: 
        :type leverable: str
        :return: dict
        """

        if self.url == 'test':
            artefactlist = ['fk-' + leverable + '_wlsapp', 'fk-' + leverable + '_tuxapp']
        else:
            artefactlist = []
            try:
                response = urlopen(
                    'http://' + self.url + '/nexus/service/local/lucene/search?repositoryId=rpm-dev&g=fk.rpm.'
                    + leverable)
            except (HTTPError, URLError) as e:
                logger.error(e)
                return ['Error getting artefacts!!!']

            metadata_root = elementTree.parse(response)
            for data in metadata_root.iter('artifact'):
                artefact = data.find('artifactId').text
                if artefact not in artefactlist:
                    artefactlist.append(artefact)

        return artefactlist

    # @staticmethod
    def get_artefactversions(self, artefact):
        """
        Gets all artefact version from artefacts
        Url is a string of host:port
        
        :param artefact:
        :type artefact: str
        :return: list
        """

        if self.url == 'test':
            artefactversionlist = [artefact + '-1.0.0-80.x86_64.rpm', artefact + '-1.0.0-81.x86_64.rpm']
        else:
            if 'fk-' in artefact:
                tmp = artefact.split('fk-')
                leverable = tmp[1].split('_')[0]
            else:
                leverable = 'tools'

            artefactversionlist = []
            try:
                response = urlopen(
                    'http://' + self.url + '/nexus/service/local/lucene/search?repositoryId=rpm-dev&g=fk.rpm.'
                    + leverable + '&a=' + artefact)
            except (HTTPError, URLError) as e:
                logger.error(e)
                return ['Error getting artefactversions!!!']

            metadata_root = elementTree.parse(response)
            for data in metadata_root.iter('artifact'):
                extension = 'x86_64.rpm'
                for ext in data.findall('.//extension'):
                    if 'rpm' in ext.text:
                        extension = ext.text
                artefactversionlist.append(artefact + '-' + '.' + extension + '.rpm')
                # artefactversiondict[data.find('version').text] = extension

        return artefactversionlist
