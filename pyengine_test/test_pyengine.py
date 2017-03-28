import unittest

from generated.QsBeans import ItemBean, MetaBean


class T(unittest.TestCase):
    def test_serial(self):
        item = ItemBean(meta=MetaBean(name='blabla'), tags=[], files=[], actions=[])
        print(item.to_string())