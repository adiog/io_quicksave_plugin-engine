import json

import pika


def rabbit_poll(queue, bean, bean_callback):
    def callback(ch, method, properties, body):
        bean_callback(bean(json.loads(body.decode())))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(callback,
                          queue=queue,
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
