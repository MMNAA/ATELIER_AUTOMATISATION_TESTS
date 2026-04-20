from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_tests():
    result = subprocess.run(
        ["python3", "-m", "pytest", "-q"],
        capture_output=True,
        text=True
    )
    status = "OK" if result.returncode == 0 else "FAIL"
    output = result.stdout.strip()

    return status, output


@app.route("/")
def dashboard():
    status, output = run_tests()

    color = "green" if status == "OK" else "red"

    return f"""
    <h1>API Monitoring Dashboard</h1>
    <p>Status: <strong style='color:{color}'>{status}</strong></p>
    <pre>{output}</pre>
    """


@app.route("/health")
def health():
    status, output = run_tests()

    return jsonify({
        "status": status,
        "details": output
    })