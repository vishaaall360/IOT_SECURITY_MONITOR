# 🌐 IoT Smart Security Monitoring & Intrusion Detection System

The **IoT Smart Security Monitoring & Intrusion Detection System** is a cyber-security and Internet of Things (IoT) based project designed to simulate a real-world smart security solution. This system monitors sensor data such as motion, temperature, and gas levels to detect intrusion and abnormal environmental conditions in real time. It generates alerts and visualizes data through a web-based dashboard.

This project demonstrates strong fundamentals in **IoT security, intrusion detection, real-time monitoring, and backend web development**, making it an excellent addition to a cyber-security or IoT-focused GitHub portfolio.

---

## 🚀 Project Objectives

- To simulate IoT sensor devices generating real-time data
- To detect unauthorized access and abnormal environmental behavior
- To generate alerts for potential security threats
- To log security events for future analysis
- To visualize sensor data and alerts on a web dashboard

---

## 🧠 How the System Works

1. **IoT Sensor Simulation**
   - A Python-based simulator generates random sensor data (motion, temperature, gas).
   - This simulates real IoT devices such as PIR sensors, temperature sensors, and gas sensors.

2. **Data Transmission**
   - The simulated IoT device sends sensor data to a central server using HTTP requests.

3. **Intrusion Detection Engine**
   - Incoming sensor data is analyzed using predefined rules.
   - If abnormal values are detected (e.g., motion detected, high temperature, gas leakage), alerts are generated.

4. **Alert Management**
   - Alerts are logged into a file for auditing and investigation.
   - Multiple alerts can be generated for a single data packet.

5. **Web Dashboard**
   - Displays live sensor data.
   - Shows intrusion alerts in real time.
   - Provides a simple and user-friendly interface.

---

## 🛠️ Technology Stack

### Backend
- Python 3
- Flask (Web Framework)

### IoT Simulation
- Python
- Requests Library

### Frontend
- HTML
- CSS

### Security Concepts
- Intrusion Detection
- Event Logging
- Sensor Data Monitoring

---

## 📁 Project Structure

iot-security-monitor/
│
├── device/
│ └── sensor_simulator.py
│
├── server/
│ ├── app.py
│ ├── detection_engine.py
│ ├── alert_manager.py
│ │
│ ├── templates/
│ │ └── dashboard.html
│ │
│ ├── static/
│ │ └── style.css
│
├── logs/
│ └── sensor.log
│
├── requirements.txt

## 📜 File Descriptions

### `sensor_simulator.py`
Simulates IoT sensors by generating random data for motion, temperature, and gas levels and sending it to the server.

### `app.py`
Main Flask application that receives sensor data, triggers detection logic, and renders the dashboard.

### `detection_engine.py`
Contains intrusion detection logic based on predefined threshold rules.

### `alert_manager.py`
Handles logging of security alerts into a log file.

### `dashboard.html`
Web interface that displays live sensor data and intrusion alerts.

### `style.css`
Styles the dashboard with a modern dark-themed UI.

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install flask requests


---

## 📜 File Descriptions

### `sensor_simulator.py`
Simulates IoT sensors by generating random data for motion, temperature, and gas levels and sending it to the server.

### `app.py`
Main Flask application that receives sensor data, triggers detection logic, and renders the dashboard.

### `detection_engine.py`
Contains intrusion detection logic based on predefined threshold rules.

### `alert_manager.py`
Handles logging of security alerts into a log file.

### `dashboard.html`
Web interface that displays live sensor data and intrusion alerts.

### `style.css`
Styles the dashboard with a modern dark-themed UI.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install flask requests

2️⃣ Start the Server

cd server
python app.py

Running on http://127.0.0.1:5000

3️⃣ Start IoT Sensor Simulator (New Terminal)

cd device
python sensor_simulator.py

4️⃣ Open Web Dashboard

http://127.0.0.1:5000

2️⃣ Start the Server

📊 Sample Alerts Detected

🚨 Motion Detected

🔥 High Temperature Detected

💨 Gas Leakage Detected

🔐 Security Relevance

This project simulates how modern IoT security systems:

Detect physical intrusion

Monitor environmental anomalies

Generate security alerts

Maintain security logs for investigation

📌 Use Cases

Smart Home Security

Industrial IoT Monitoring

Smart Building Surveillance

Cyber-Security Training

Academic Mini / Final Year Projects

📌 Use Cases

Smart Home Security

Industrial IoT Monitoring

Smart Building Surveillance

Cyber-Security Training

Academic Mini / Final Year Projects

👨‍💻 Author

Vishaal S
GitHub: https://github.com/vishaal360

⭐ Acknowledgements

This project was built for learning and demonstrating IoT security and intrusion detection concepts.

If you find this project useful, please ⭐ star the repository!


---

If you want next, I can:
- Add **PROJECT REPORT / SRS / DESIGN / TEST REPORT**
- Convert this into **AI-based IoT IDS**
- Prepare **viva questions & answers**
- Suggest the **next elite cyber + IoT project**

Just tell me 👍
