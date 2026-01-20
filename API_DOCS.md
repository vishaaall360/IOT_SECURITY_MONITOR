# API Documentation

## POST /data
Receives sensor data from IoT devices.

### Request Body (JSON)
{
  "motion": 1,
  "temperature": 45,
  "gas": 320
}

### Response
{
  "status": "received"
}

## GET /
Displays the monitoring dashboard.
