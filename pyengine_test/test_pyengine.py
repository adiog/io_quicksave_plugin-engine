import unittest

from PluginEngine import main
from generated.QsBeans import ItemBean, MetaBean, InternalCreateRequestBean, CreateRequestBean


class T(unittest.TestCase):
    def test_serial(self):
        meta = MetaBean(name='blabla')
        createRequest = CreateRequestBean(meta=meta)
        internalCreateRequest = InternalCreateRequestBean(createRequest=createRequest, storageConnectionString='', keys=[])
        main(internalCreateRequest)
