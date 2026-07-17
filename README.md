# 🚚 LogiRoute

**LogiRoute** is a real-time fleet monitoring and logistics analytics platform that simulates delivery vehicles, streams telemetry through Apache Kafka, processes it using Apache Spark Structured Streaming, stores processed data in PostgreSQL, and visualizes the fleet on a live React dashboard.

---

# Features

- 🚚 Real-time fleet simulation
- 📡 Live vehicle telemetry streaming
- ⚡ Apache Kafka event streaming
- 🔥 Apache Spark Structured Streaming
- 🗄 PostgreSQL data storage
- 🌐 FastAPI REST APIs
- 🖥 React Dashboard
- 🗺 Live vehicle map
- ⛽ Fuel consumption simulation
- 🛣 Remaining distance calculation
- ⏱ ETA calculation
- 🚨 Live alerts
  - Low Fuel
  - Overspeed
  - Delivery Completed

---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy

## Streaming
- Apache Kafka
- Apache Spark Structured Streaming

## Database
- PostgreSQL
- PostGIS

## Frontend
- React
- Bootstrap
- React Leaflet

## Infrastructure
- Docker
- Docker Compose

---

# Architecture

```
Vehicle Simulator
        │
        ▼
 Apache Kafka
        │
        ▼
Apache Spark
(Structured Streaming)
        │
        ▼
 PostgreSQL
        │
        ▼
    FastAPI
        │
        ▼
 React Dashboard
```

---

# Folder Structure

```
LogiRoute/

├── backend/
├── frontend/
├── simulator/
├── spark/
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# Prerequisites

Install the following:

- Docker Desktop
- Python 3.11+
- Node.js
- Git

---

# Clone Repository

```bash
git clone <repository-url>

cd LogiRoute
```

---

# Start Docker Services

```bash
docker compose up -d
```

Verify containers are running

```bash
docker ps
```

Expected containers

- PostgreSQL
- pgAdmin
- Kafka
- Kafka UI
- Zookeeper
- Spark

---

# Running the Project

Open **four terminals**.

---

## Terminal 1 — Vehicle Simulator

```bash
cd simulator

python main.py
```

---

## Terminal 2 — Spark Streaming

Enter the Spark container

```bash
docker exec -it logiroute-spark bash
```

Inside the container

```bash
cd /opt/logiroute/spark

python main.py
```

---

## Terminal 3 — Backend API

```bash
cd backend

uvicorn app.main:app --reload
```

---

## Terminal 4 — Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# Access URLs

## Dashboard

```
http://localhost:5173
```

---

## FastAPI

```
http://localhost:8000
```

---

## Swagger UI

```
http://localhost:8000/docs
```

---

## Kafka UI

```
http://localhost:8080
```

---

## pgAdmin

```
http://localhost:5050
```

---

# Demo Scenario

When the simulator starts, five delivery vehicles are initialized.

The fleet demonstrates different operational scenarios:

- 🚚 Two vehicles moving normally
- ⛽ One vehicle with low fuel
- 🚨 One overspeeding vehicle
- ✅ One vehicle already arrived at destination

Telemetry is streamed continuously through Kafka, processed by Spark, stored in PostgreSQL, and displayed live on the dashboard.

---

# Dashboard Features

- Fleet KPI Cards
- Live Vehicle Table
- Search Vehicles
- Live Alerts
- Vehicle Status Badges
- ETA
- Remaining Distance
- Fuel Level
- Speed
- Live Map

---

# APIs

| Endpoint | Description |
|----------|-------------|
| /fleet/live | Latest fleet telemetry |
| /routes/{id} | Route information |

---

# Future Enhancements

- Multiple delivery routes
- Fleet analytics dashboard
- Historical trip analytics
- Authentication
- Driver performance scoring
- Predictive ETA using Machine Learning

---

# Screenshots

Add screenshots here.

```
docs/

dashboard.png

map.png

alerts.png

kafka-ui.png

swagger.png

architecture.png
```

---

# Troubleshooting

## Kafka not running

```bash
docker compose up -d
```

---

## Spark not processing messages

Restart Spark inside the container.

```bash
docker exec -it logiroute-spark bash

cd /opt/logiroute/spark

python main.py
```

---

## Frontend not loading

Install dependencies

```bash
npm install
```

Then

```bash
npm run dev
```

---

## PostgreSQL not updating

Verify Spark is running and writing batches successfully.

Check PostgreSQL

```sql
SELECT * FROM vehicle_telemetry;
```

---

# Author

Ashmit Narkhede

BE Information Technology

Savitribai Phule Pune University

Project: LogiRoute
