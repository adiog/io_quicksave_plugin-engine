# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import time

from pyengine.generated.QsBeans import ItemBean
from task.git import git
from task.thumbnail import thumbnail
from task.wget import wget
from task.youtube import youtube
from util.logger import log
from util.timer import Timer
from pyqueue.pyqueue import pop


def task(name, item):
    if name == 'git':
        git(item)
    if name == 'thumbnail':
        thumbnail(item)
    elif name == 'wget':
        wget(item)
    elif name == 'youtube':
        youtube(item)
    else:
        log('WARNING: Unsupported task type: <%s>' % name)


def main():
    while True:
        async_spec = pop()
        if async_spec:
            item = ItemBean(async_spec['item'])
            with Timer('%s(item_id=%s, title="%s")' % (async_spec['task'], item.item_id, item.title[:60])):
                task(async_spec['task'], item)
        else:
            log()
            time.sleep(1)


if __name__ == '__main__':
    main()
