# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import json
import os
from queuelib import FifoDiskQueue


fifo_disk_queue_file = os.environ.get('IO_QUICKSAVE_CDN_DIR', '.') + '/queuefile'


def push(async_spec):
    queue = FifoDiskQueue(fifo_disk_queue_file)
    queue.push(json.dumps(async_spec).encode())
    queue.close()


def pop():
    queue = FifoDiskQueue(fifo_disk_queue_file)
    async_spec_bytes = queue.pop()
    queue.close()
    if async_spec_bytes:
        return json.loads(async_spec_bytes.decode())
    else:
        return None
