# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import hashlib
import os
import random
import datetime

from generated.QsBeans import TagBean, RichItemBean

from pyqueue.pyqueue import push


def get_fs_dir():
    return os.environ.get('IO_QUICKSAVE_CDN_DIR', '.')


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
    print(itemBean.to_json())
    if itemBean.item_type == 'page':
        push({'task': 'thumbnail', 'item': itemBean.to_json()})
        push({'task': 'wget', 'item': itemBean.to_json()})
    print(itemBean.source_url)
    if 'youtube.com' in itemBean.source_url:
        print('youtube')
        push({'task': 'youtube', 'item': itemBean.to_json()})
    if 'github.com' in itemBean.source_url:
        print('github')
        push({'task': 'git', 'item': itemBean.to_json()})
    tags = [TagBean(name='chrome')]
    if ('wikipedia' in itemBean.source_url):
        tags.append(TagBean(name='wiki'))

    return RichItemBean(item=itemBean, tags=tags)
