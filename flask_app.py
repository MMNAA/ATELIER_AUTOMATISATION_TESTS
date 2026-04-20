from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>API Monitoring</h1>
    <a href="/health">Voir l'état</a>
    """

@app.route("/health")
def health():
    result = subprocess.run(
        ["python3", "-m", "pytest", "-q"],
        capture_output=True,
        text=True
    )

    return jsonify({
        "status": "OK" if result.returncode == 0 else "FAIL",
        "details": result.stdout
    })