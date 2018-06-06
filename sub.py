import time

from google.cloud import pubsub_v1

project_name = 'noble-freehold-195108'
topic_name = 'topic1'
subscription_names = ['sub1', 'sub2', 'sub3']

subscriber = pubsub_v1.SubscriberClient()


def callback1(message):
    t = time.time()
    print(
        'Received message: {}, date: {}, latency: {}'.format(message, t, float(t) - float(message.attributes['time'])))
    if message.attributes['origin'] != 'topic1':
        raise ValueError('Error: Expected topic1, got {}'.format(message.attributes['origin'] != 'topic1'))
    message.ack()


def callback2(message):
    t = time.time()
    print(
        'Received message: {}, date: {}, latency: {}'.format(message, t, float(t) - float(message.attributes['time'])))
    if message.attributes['origin'] != 'topic2':
        raise ValueError('Error: Expected topic1, got {}'.format(message.attributes['origin'] != 'topic1'))
    message.ack()


def callback3(message):
    t = time.time()
    print(
        'Received message: {}, date: {}, latency: {}'.format(message, t,
                                                             float(t) - float(message.attributes['time'])))
    if message.attributes['origin'] != 'topic3':
        raise ValueError('Error: Expected topic1, got {}'.format(message.attributes['origin'] != 'topic1'))
    message.ack()


subscription_path1 = subscriber.subscription_path(project_name, subscription_names[0])
print('Listening for messages on {}'.format(subscription_path1))
subscriber.subscribe(subscription_path1, callback=callback1)

subscription_path2 = subscriber.subscription_path(project_name, subscription_names[1])
print('Listening for messages on {}'.format(subscription_path2))
subscriber.subscribe(subscription_path2, callback=callback2)

subscription_path3 = subscriber.subscription_path(project_name, subscription_names[2])
print('Listening for messages on {}'.format(subscription_path3))
subscriber.subscribe(subscription_path3, callback=callback3)

while True:
    time.sleep(60)
