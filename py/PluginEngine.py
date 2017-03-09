# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import hashlib
import os
import random
import datetime

from Selenium import save_screenshot
from generated.QsBeans import TagBean, RichItemBean


def get_fs_dir():
    return '/fs.quicksave.io'


def UUID():
    return hashlib.sha224('%s%s' % (random.random(), datetime.datetime.now())).hexdigest()


def get_dir(uuid):
    dir = get_fs_dir() + '/' + uuid
    os.makedirs(dir)
    return dir


def main(item, itemBean):
    uuid = UUID()
    dir = get_dir(uuid)
    if item.item_type == 'page':
        save_screenshot(item.source_url, dir + '/screenshot.png')
    tags = [TagBean(name='chrome')]
    if ('wikipedia' in itemBean.source_url):
        tags.append(TagBean(name='wiki'))
    return RichItemBean(item=itemBean, tags=tags)
