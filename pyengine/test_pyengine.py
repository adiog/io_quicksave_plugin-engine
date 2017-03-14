import unittest

from beans import ItemBean


class PyEngineTestCase(unittest.TestCase):
    def test_bean(self):
        item = ItemBean('{"freetext": "blabla"}')
        print(item.to_string())