from flask import Flask, request, jsonify, abort
from google.cloud import pubsub_v1

app = Flask(__name__)

project_name = 'noble-freehold-195108'
topic_name = 'topic1'
subscription_name = 'sub1'

batch_settings = pubsub_v1.types.BatchSettings(
    max_bytes=1024,  # One kilobyte
    max_latency=1,  # One second
)

publisher = pubsub_v1.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project_name, topic_name)


@app.route('/pubsub/topic1', methods=['POST'])
def pushtotopic():
    if not request.json or not 'data' in request.json:
        abort(400)

    data = request.data.encode('utf-8')
    publisher.publish(topic_path, data, origin='python-sample', username='gcp')

    return jsonify({'result': 'OK'}), 200


if __name__ == '__main__':
    app.run(port='6666', threaded=True)
