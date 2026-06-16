# API Documentation

## Base URL

```text
http://localhost:8000
```

---

## Health Check

### Request

```http
GET /
```

### Response

```json
{
  "status": "running",
  "project": "smart-infra-platform"
}
```

---

## Latest Metric

### Request

```http
GET /metrics/latest
```

### Response

```json
{
  "id": 1039,
  "server_id": 5,
  "cpu": 0.1,
  "ram": 16.2,
  "disk": 1.2,
  "created_at": "2026-06-15 13:25:40.968327+00:00"
}
```

---

## Latest Anomaly

### Request

```http
GET /anomalies/latest
```

### Response

```json
{
  "id": 1039,
  "metric_id": 1039,
  "cpu_status": "normal",
  "ram_status": "normal",
  "disk_status": "normal"
}
```

Possible values:

```text
normal
warning
critical
```

---

## Latest ML Prediction

### Request

```http
GET /ml-predictions/latest
```

### Response

```json
{
  "id": 166,
  "metric_id": 1039,
  "prediction": "normal"
}
```

Possible values:

```text
normal
anomaly
```

---

## System Health

### Request

```http
GET /system/health
```

### Response

```json
{
  "status": "healthy",
  "latest_metric_id": 1039,
  "cpu_status": "normal",
  "ram_status": "normal",
  "disk_status": "normal"
}
```

Possible values:

```text
healthy
warning
critical
```

---

## Data Sources

The API serves data from PostgreSQL tables:

* metrics
* anomalies
* ml_predictions
* automation_logs

---

## Typical Workflow

1. Monitoring Agent collects metrics
2. FastAPI receives metrics
3. PostgreSQL stores data
4. ML Engine generates predictions
5. Automation Engine evaluates rules
6. Grafana visualizes results
