import json
from queuelib import FifoDiskQueue


fifo_disk_queue_file = '/fs.quicksave.io/queuefile'

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
