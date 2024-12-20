from flask import Flask, jsonify
from flask_socketio import SocketIO
import random

HOST, PORT = "127.0.0.1", 5000

app = Flask(__name__)
socketio = SocketIO(app)


def randomOffset(K):
    x = random.uniform(-K, K)
    y = random.uniform(-K, K)
    return x, y


@app.route('/nodes', methods=['GET'])
def get_nodes():
    try:
        nodes = [
            {"id": 0, "x": 411.18324, "y": 351.84357},
            {"id": 1, "x": 440.32921, "y": 303.0037},
            {"id": 2, "x": 458.66425, "y": 303.54155},
            {"id": 3, "x": 471.87874, "y": 305.14463},
            {"id": 4, "x": 380.07385, "y": 302.16328},
            {"id": 5, "x": 364.53545, "y": 302.17561},
            {"id": 6, "x": 346.99638, "y": 302.48978},
            {"id": 7, "x": 482.18208, "y": 320.18712},
            {"id": 8, "x": 316.28693, "y": 319.23223},
            {"id": 9, "x": 438.36536, "y": 396.02368},
            {"id": 10, "x": 374.93111, "y": 393.30462},
            {"id": 11, "x": 543.8813, "y": 503.34543},
            {"id": 12, "x": 220.56227, "y": 472.70682},
            {"id": 13, "x": 569.93549, "y": 728.50897},
            {"id": 14, "x": 141.85921, "y": 684.17467},
            {"id": 15, "x": 553.67516, "y": 836.02129},
            {"id": 16, "x": 127.72606, "y": 750.37777},
            {"id": 17, "x": 565.93933, "y": 871.31939},
            {"id": 18, "x": 104.53485, "y": 771.007},
            {"id": 19, "x": 548.56079, "y": 854.48513},
            {"id": 20, "x": 125.90061, "y": 760.63042},
            {"id": 21, "x": 538.12325, "y": 841.22583},
            {"id": 22, "x": 140.92481, "y": 752.8244},
            {"id": 23, "x": 460.96134, "y": 935.05262},
            {"id": 24, "x": 261.88452, "y": 919.69769},
            {"id": 25, "x": 463.49892, "y": 1296.83681},
            {"id": 26, "x": 277.00207, "y": 1269.07814},
            {"id": 27, "x": 423.80653, "y": 1611.25935},
            {"id": 28, "x": 250.25169, "y": 1595.48218},
            {"id": 29, "x": 424.84478, "y": 1673.79524},
            {"id": 30, "x": 242.06125, "y": 1655.71953},
            {"id": 31, "x": 372.44869, "y": 1658.55686},
            {"id": 32, "x": 279.27225, "y": 1657.49199}
        ]
        offsetX, offsetY = randomOffset(20)
        return jsonify({
            'nodes': [{
                'nodeId': node['id'],
                'x': round(node['x'] + offsetX, 5),
                'y': round(node['y'] + offsetY, 5)
            } for node in nodes]
        })
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    socketio.run(app, host=HOST, port=PORT)
