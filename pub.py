from flask import Flask, request, jsonify, abort
from google.cloud import pubsub

app = Flask(__name__)

project_name = 'inspired-bus-194216'
topic_name = 'mytopic'
subscription_name = 'sub1'

batch_settings = pubsub.types.BatchSettings(
    max_bytes=1024,  # One kilobyte
    max_latency=1,  # One second
)

publisher = pubsub.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project_name, topic_name)


@app.route('/pubsub/topic1', methods=['POST'])
def pushtotopic():
    if not request.json or not 'data' in request.json:
        abort(400)

    data = request.data
    publisher.publish(topic_path, data)
    print("{0}".format(data))
    return jsonify({'result': 'OK'}), 200


if __name__ == '__main__':
    app.run(port='6666', threaded=True,debug=True)
