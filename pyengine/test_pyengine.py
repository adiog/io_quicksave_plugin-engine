import unittest

from beans import MetaBean


class PyEngineTestCase(unittest.TestCase):
    def test_bean(self):
        item = MetaBean('{"freetext": "blabla"}')
        print(item.to_string())