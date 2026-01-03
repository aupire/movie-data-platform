from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)


@app.route("/", methods=["GET"])
def echo_get_params():
    """
    Renvoie tous les paramètres GET reçus sous forme JSON.
    """
    params = request.args.to_dict(flat=True)
    return jsonify(params), 200


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
