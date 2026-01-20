def detect_intrusion(data):
    alerts = []

    if data["motion"] == 1:
        alerts.append("🚨 Motion Detected")

    if data["temperature"] > 50:
        alerts.append("🔥 High Temperature Detected")

    if data["gas"] > 400:
        alerts.append("💨 Gas Leakage Detected")

    return alerts
