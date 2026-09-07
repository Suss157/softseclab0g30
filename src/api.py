from flask import Flask, jsonify

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> 9784433c940b4ea819eca7b41475a74f7d6375c1
