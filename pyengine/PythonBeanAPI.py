# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

from PluginEngine import main
from generated.QsBeans import InternalCreateRequestBean, MetaBean, TagBean, ItemBean, MessageBean
from pybeans import to_string


def process(internalCreateRequestBean):
    return main(internalCreateRequestBean)

