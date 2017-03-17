# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import time

from pyengine.generated.QsBeans import ItemBean, TaskBean, DoneTaskBean
from rabbit_poll import rabbit_poll
from rabbit_push import rabbit_push
from task.git import git
from task.thumbnail import thumbnail
from task.wget import wget
from task.youtube import youtube
from util.logger import log
from util.timer import Timer

def task(name, item):
    if name == 'git':
        git(item)
    elif name == 'thumbnail':
        thumbnail(item)
    elif name == 'wget':
        wget(item)
    elif name == 'youtube':
        youtube(item)
    else:
        log('WARNING: Unsupported task type: <%s>' % name)


def task_callback(task_bean):
    with Timer('%s' % (task_bean.name)):
        task(task_bean.name, task_bean.item)
        rabbit_push('response', DoneTaskBean(name=('done [%s]' % task_bean.name)))

def main():
    rabbit_poll('request', TaskBean, task_callback)


if __name__ == '__main__':
    main()
