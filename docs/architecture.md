# Smart Infrastructure Platform Architecture

## Overview

The Smart Infrastructure Platform is a self-healing infrastructure monitoring system built with Python, Docker, PostgreSQL, Grafana, Machine Learning, and Ansible.

The platform continuously collects infrastructure metrics, detects anomalies, generates machine learning predictions, and automatically executes remediation actions.

---

## Components

### Monitoring Agent

The monitoring agent collects:

* CPU usage
* RAM usage
* Disk usage

The agent sends collected metrics to the FastAPI backend.

---

### FastAPI Backend

The backend provides:

* Metric ingestion
* Data persistence
* REST API endpoints
* Health monitoring endpoints

---

### PostgreSQL Database

PostgreSQL serves as the central data store.

Stored data includes:

* Metrics
* Rule-based anomalies
* Machine learning predictions
* Automation logs

---

### Grafana

Grafana visualizes:

* CPU metrics
* RAM metrics
* Disk metrics
* Anomaly counts
* ML prediction statistics

---

### Machine Learning Engine

The ML engine uses Isolation Forest for anomaly detection.

Responsibilities:

* Model training
* Prediction generation
* Prediction persistence

---

### Automation Engine

The automation engine evaluates infrastructure rules and determines corrective actions.

Examples:

* Restart Docker
* Restart Apache
* Cleanup disk space

---

### Ansible

Ansible executes infrastructure remediation actions through playbooks.

---

## Data Flow

Monitoring Agent
→ FastAPI Backend
→ PostgreSQL

PostgreSQL
→ Grafana

PostgreSQL
→ ML Engine
→ ML Predictions

PostgreSQL
→ Automation Engine
→ Ansible Playbooks
→ Infrastructure Actions

---

## Self-Healing Workflow

1. Collect infrastructure metrics
2. Store metrics in PostgreSQL
3. Generate ML predictions
4. Evaluate automation rules
5. Execute Ansible playbooks
6. Log automation actions
7. Prevent duplicate execution
