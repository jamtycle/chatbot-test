import os
from flask import Flask, jsonify, request, send_file
from werkzeug.exceptions import HTTPException
from chatai import chatbot


app = Flask(__name__)
_ = os.system("clear")


@app.route("/")
def index():
    return jsonify({"message": "Hello World"})


@app.route("/chat/ask", methods=["GET"])
def count_grapes():
    input = request.args.get("input") or ""
    return jsonify(chatbot(input))


app.run()
