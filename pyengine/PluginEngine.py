# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import hashlib
import os
import random
import datetime
import time

from generated.QsBeans import TagBean, MetaBean, ItemBean, BackgroundTaskBean

from pyqueue.pyqueue import push, pop, fifo_disk_response_queue_file
from pyqueue.pyqueue import fifo_disk_request_queue_file
from rabbit_push import rabbit_push


def get_fs_dir():
    return os.environ.get('IO_QUICKSAVE_CDN_DIR', '.')


def UUID():
    return hashlib.sha224(('%s%s' % (random.random(), datetime.datetime.now())).encode()).hexdigest()


def get_dir(uuid):
    dir = get_fs_dir() + '/' + uuid
    os.makedirs(dir)
    return dir



def main(metaBean):
    print(metaBean.to_json())
    if metaBean.meta_type == 'page':
        rabbit_push('request', BackgroundTaskBean(name='thumbnail', meta=metaBean, kwargs='{}'))
        rabbit_push('request', BackgroundTaskBean(name='wget', meta=metaBean, kwargs='{}'))
    print(metaBean.source_url)
    tags = [TagBean(name='chrome')]
    if metaBean.source_url is not None:
        if 'youtube.com' in metaBean.source_url:
            print('youtube')
            rabbit_push('request', BackgroundTaskBean(name='youtube', meta=metaBean, kwargs='{}'))
        if 'github.com' in metaBean.source_url:
            print('github')
            rabbit_push('request', BackgroundTaskBean(name='git', meta=metaBean, kwargs='{}'))
        if ('wikipedia' in metaBean.source_url):
            tags.append(TagBean(name='wiki'))

    item = ItemBean(meta=metaBean, tags=tags, files=[], actions=[])
    #print(item.to_string())
    return item


def do_donetask(messageBean):
    while True:
        tsk = pop(fifo_disk_response_queue_file)
        if tsk:
            messageBean.message = tsk
            return messageBean
        else:
            time.sleep(1)