from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "API Monitoring is running"

@app.route("/health")
def health():
    result = subprocess.run(
        ["pytest"],
        capture_output=True,
        text=True
    )

    return jsonify({
        "status": "OK" if result.returncode == 0 else "FAIL",
        "tests": result.stdout
    })