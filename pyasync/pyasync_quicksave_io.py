import os
import subprocess
import time

import datetime

from pyasync.crop_image import crop_image
from pyasync.selenium_thumbnail import save_thumbnail
from pyqueue.pyqueue import pop


def log(message=''):
    print(datetime.datetime.now().strftime("[%d/%m/%Y %H:%M:%S] ") + message)


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
        print('                      Result: %sμs' % (self.end - self.start))
        print()


def task(name, hash, argument):
    if name == 'thumbnail':
        thumbnail_file = '/fs.quicksave.io/%s/thumbnail.png' % hash
        thumbnail_crop = '/fs.quicksave.io/%s/thumbnail_crop.png' % hash
        save_thumbnail(url=argument, thumbnail_file=thumbnail_file)
        crop_image(thumbnail_file, thumbnail_crop)
    elif name == 'youtube':
        #video_file = '/fs_quicksave_io/%s/video_%%(title)s' % hash
        video_file = '/fs.quicksave.io/%s/video' % hash
        ret_code = subprocess.check_output(['youtube-dl', '--output', video_file, argument])
    else:
        print('nothing to do')


def main():
    while True:
        async_spec = pop()
        if async_spec:
            with Timer('%s("%s", "%s")' % (async_spec['task'], async_spec['hash'][:10], async_spec['argument'][:100])):
                task(async_spec['task'], async_spec['hash'], async_spec['argument'])
        else:
            log()
            time.sleep(10)


if __name__ == '__main__':
    main()
