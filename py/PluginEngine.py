# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import hashlib
import os
import random
import datetime

from generated.QsBeans import TagBean, RichItemBean

from pyqueue.pyqueue import push


def get_fs_dir():
    return '/fs.quicksave.io'


def UUID():
    return hashlib.sha224(('%s%s' % (random.random(), datetime.datetime.now())).encode()).hexdigest()


def get_dir(uuid):
    dir = get_fs_dir() + '/' + uuid
    os.makedirs(dir)
    return dir


def main(itemBean):
    uuid = UUID()
    dir = get_dir(uuid)
    itemBean.url = uuid
    if itemBean.item_type == 'page':
        push({'task': 'thumbnail', 'hash': uuid, 'argument': itemBean.source_url})
    print(itemBean.source_url)
    if 'youtube.com' in itemBean.source_url:
        print('youtube')
        push({'task': 'youtube', 'hash': uuid, 'argument': itemBean.source_url})
    tags = [TagBean(name='chrome')]
    if ('wikipedia' in itemBean.source_url):
        tags.append(TagBean(name='wiki'))

    return RichItemBean(item=itemBean, tags=tags)
