# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import os


def get_fs_dir():
    return os.environ.get('IO_QUICKSAVE_CDN_DIR', '.')


class Provider(object):
    def __init__(self, item):
        self.item = item
        self.path = ''

    def __enter__(self):
        self.path = get_fs_dir() + '/%s' % self.item.item_id
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
