def log_alert(alert):
    with open("logs/sensor.log", "a") as f:
        f.write(alert + "\n")
