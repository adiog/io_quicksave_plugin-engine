# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

from PluginEngine import main, do_donetask
from generated.QsBeans import ItemBean, TagBean, RichItemBean, MessageBean
from pybeans import to_string


def process(itemBean):
    return main(itemBean)


def donetask(messageBean):
    return do_donetask(messageBean)


