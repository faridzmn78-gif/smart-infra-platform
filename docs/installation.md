# Installation Guide

## Prerequisites

Before running the project, install the following tools:

* Docker
* Docker Compose
* Python 3.12+
* Git

Optional:

* Ansible
* WSL (Windows users)

---

## Clone Repository

```bash
git clone https://github.com/your-username/smart-infra-platform.git

cd smart-infra-platform
```

---

## Start Infrastructure

Run all services:

```bash
docker compose up -d --build
```

Verify containers:

```bash
docker ps
```

Expected services:

* backend
* postgres
* agent
* ml-engine
* grafana

---

## Backend Health Check

```bash
curl http://localhost:8000
```

Expected response:

```json
{
  "status": "running",
  "project": "smart-infra-platform"
}
```

---

## Grafana

Open:

http://localhost:3000

Default credentials:

Username:

```text
admin
```

Password:

```text
admin
```

---

## API Endpoints

Latest Metric:

```text
GET /metrics/latest
```

Latest Anomaly:

```text
GET /anomalies/latest
```

Latest ML Prediction:

```text
GET /ml-predictions/latest
```

System Health:

```text
GET /system/health
```

---

## Automation Engine

Execute manually:

```bash
python automation/live_engine.py
```

The engine:

* Evaluates infrastructure rules
* Executes Ansible playbooks
* Logs actions
* Prevents duplicate execution

---

## Machine Learning

Train model:

```bash
python ml-engine/train.py
```

Generate prediction:

```bash
python ml-engine/predict_and_save.py
```
