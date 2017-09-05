# This file is a part of quicksave project.
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


def UUID():
    return hashlib.sha224(('%s%s' % (random.random(), datetime.datetime.now())).encode()).hexdigest()


def main(internalCreateRequestBean):
    createRequestBean = internalCreateRequestBean.createRequest
    metaBean = createRequestBean.meta
    print(metaBean.to_json())
    if metaBean.meta_type == 'page':
        rabbit_push('request', BackgroundTaskBean(name='thumbnail', internalCreateRequest=internalCreateRequestBean, kwargs='{}'))
        rabbit_push('request', BackgroundTaskBean(name='wget', internalCreateRequest=internalCreateRequestBean, kwargs='{}'))
    print(metaBean.source_url)
    tags = [TagBean(name='python_sync')]
    if metaBean.source_url is not None:
        if 'youtube.com' in metaBean.source_url:
            print('youtube')
            rabbit_push('request', BackgroundTaskBean(name='youtube', internalCreateRequest=internalCreateRequestBean, kwargs='{}'))
        if 'github.com' in metaBean.source_url:
            print('github')
            rabbit_push('request', BackgroundTaskBean(name='git', internalCreateRequest=internalCreateRequestBean, kwargs='{}'))
        if ('wikipedia' in metaBean.source_url):
            tags.append(TagBean(name='wiki'))

    item = ItemBean(meta=metaBean, tags=tags, files=[], actions=[])
    #print(item.to_string())
    return item

