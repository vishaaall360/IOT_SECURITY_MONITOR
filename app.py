from flask import Flask, render_template, request
from detection_engine import detect_intrusion
from alert_manager import log_alert

app = Flask(__name__)

latest_data = {}
alerts = []

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        data=latest_data,
        alerts=alerts
    )

@app.route("/data", methods=["POST"])
def receive_data():
    global latest_data, alerts
    data = request.json
    latest_data = data

    alerts = detect_intrusion(data)

    for alert in alerts:
        log_alert(alert)

    return {"status": "received"}

if __name__ == "__main__":
    app.run(debug=True)
