import unittest
from lib.nexus_class import NexusHelperClass


class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.nexusHelper = NexusHelperClass('url')

    def test_get_nexus_repos(self):

        self.assertIsInstance(self.nexusHelper.get_repos(), list)

    def test_get_nexus_leverables(self):

        self.assertIsInstance(self.nexusHelper.get_leverables(), list)

    def test_get_nexus_artefacts(self):

        self.assertIsInstance(self.nexusHelper.get_artefacts([]), dict)

    def test_get_nexus_artefactversions(self):

        self.assertIsInstance(self.nexusHelper.get_artefactversions({}), dict)

if __name__ == '__main__':
    unittest.main()
