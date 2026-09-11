from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})
from src.calculator import Calculator

calculator = Calculator()

@app.route("/calc", methods=["POST"])
def calc():
    data = request.get_json()
    expression = data.get("expression")
    result = calculator.calc(expression)
    return jsonify({"expression": expression, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

