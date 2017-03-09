import os
import subprocess
import time

from pyasync.selenium_thumbnail import save_thumbnail
from pyqueue.pyqueue import pop

def task(name, hash, argument):
    if name == 'thumbnail':
        thumbnail_file = '/fs.quicksave.io/%s/thumbnail.png' % hash
        save_thumbnail(url=argument, thumbnail_file=thumbnail_file)
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
            print(async_spec['task'], async_spec['argument'])
            task(async_spec['task'], async_spec['hash'], async_spec['argument'])
        else:
            print('inactive')
            time.sleep(2)

if __name__ == '__main__':
    main()
