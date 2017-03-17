# This file is a part of quickave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import hashlib
import os
import random
import datetime
import time

from generated.QsBeans import TagBean, RichItemBean, TaskBean

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



def main(itemBean):
    uuid = UUID()
    dir = get_dir(uuid)
    itemBean.url = uuid
    print(itemBean.to_json())
    if itemBean.item_type == 'page':
        rabbit_push('request', TaskBean(name='thumbnail', item=itemBean))
        rabbit_push('request', TaskBean(name='wget', item=itemBean))
    print(itemBean.source_url)
    if 'youtube.com' in itemBean.source_url:
        print('youtube')
        rabbit_push('request', TaskBean(name='youtube', item=itemBean))
    if 'github.com' in itemBean.source_url:
        print('github')
        rabbit_push('request', TaskBean(name='git', item=itemBean))
    tags = [TagBean(name='chrome')]
    if ('wikipedia' in itemBean.source_url):
        tags.append(TagBean(name='wiki'))

    return RichItemBean(item=itemBean, tags=tags)


def do_donetask(messageBean):
    while True:
        tsk = pop(fifo_disk_response_queue_file)
        if tsk:
            messageBean.message = tsk
            return messageBean
        else:
            time.sleep(1)