from flask import Flask, request, jsonify


# Init app
app = Flask(__name__)


@app.route('/', methods=['POST'])
def route_creation():
    cards = request.json['cards']
    return jsonify({'cards': cards})


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
