from oceanic import app
from flask import Response,Request, jsonify

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})