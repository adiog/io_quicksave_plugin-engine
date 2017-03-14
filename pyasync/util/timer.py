# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import datetime

from util.logger import log


class Timer(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = datetime.datetime.now()
        print()
        log('%s ...' % self.message)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        log('... %s' % (self.message))
        print('                      Time: %sμs' % (self.end - self.start))
        print()