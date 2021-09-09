import unittest

import stactools.worldhistclim


class TestModule(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(stactools.worldhistclim.__version__)
