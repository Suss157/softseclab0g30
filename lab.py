from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/hello")
def hello() -> tuple[dict[str, str], int]:
    return jsonify({"message": "Hello world!"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
