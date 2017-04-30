# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import time

from pyengine.generated.QsBeans import MetaBean, BackgroundTaskBean
from rabbit_poll import rabbit_poll
from rabbit_push import rabbit_push
from task.git import git
from task.thumbnail import thumbnail
from task.wget import wget
from task.youtube import youtube
from util.logger import log
from util.storage import Sshfs
from util.timer import Timer


def task(name, internalCreateRequest, params):
    meta = internalCreateRequest.createRequest.meta

    sshfs = Sshfs(internalCreateRequest.storageConnectionString, meta.user_hash, internalCreateRequest.keys)
    sshfs.init(meta.meta_hash)

    if name == 'git':
        return git(internalCreateRequest, sshfs)
    elif name == 'thumbnail':
        return thumbnail(internalCreateRequest, sshfs)
    elif name == 'wget':
        return wget(internalCreateRequest, sshfs)
    elif name == 'youtube':
        return youtube(internalCreateRequest, sshfs)
    else:
        log('WARNING: Unsupported task type: <%s>' % name)
        return []


def task_callback(task_bean):
    with Timer('%s' % (task_bean.name)):
        database_tasks = task(task_bean.name, task_bean.internalCreateRequest, task_bean.kwargs)
        for database_task in database_tasks:
            rabbit_push('response', database_task)

def main():
    rabbit_poll('request', BackgroundTaskBean, task_callback)


if __name__ == '__main__':
    main()
