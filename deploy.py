from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route("/generate_code", methods=["POST"])
def generate_code():
    data = request.json
    prompt = data.get("prompt", "")
    code = main.generate_code(prompt)
    return jsonify({"code": code})

@app.route("/debug_code", methods=["POST"])
def debug_code():
    data = request.json
    code = data.get("code", "")
    debugged_code = main.debug_code(code)
    return jsonify({"debugged_code": debugged_code})

@app.route("/explain_code", methods=["POST"])
def explain_code():
    data = request.json
    code = data.get("code", "")
    explanation = main.explain_code(code)
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(debug=True)
