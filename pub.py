import random
import time

from flask import Flask, request, jsonify, abort
from google.cloud import pubsub

app = Flask(__name__)

project_name = 'noble-freehold-195108'
topic_names = ['topic1', 'topic2', 'topic3']

batch_settings = pubsub.types.BatchSettings(
    max_messages=1000,
    # max_bytes=1024,
    max_latency=0.1,
)

publisher = pubsub.PublisherClient(batch_settings)


@app.route('/pubsub/topic1', methods=['POST'])
def pushtotopic():
    if not request.json or not 'data' in request.json:
        abort(400)

    t = time.time()
    data = '{}, date: {}'.format(request.data.encode('utf-8'), t)

    topic_name = topic_names[random.randint(0, 10000) % len(topic_names)]
    print topic_name
    topic_path = publisher.topic_path(project_name, topic_name)
    publisher.publish(topic_path, data, origin='{}'.format(topic_name), time='{}'.format(t))

    return jsonify({'result': 'OK'}), 200


if __name__ == '__main__':
    app.run(port='6666', threaded=True)
