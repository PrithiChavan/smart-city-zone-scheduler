# Task 9 — Distributed Architecture & Communication Plan

## 1. Architecture Choice

### Hybrid Distributed Architecture

The Smart City system will use a **Hybrid Architecture**.

Each zone (Zone-A, Zone-B and Zone-C) has its own local
controller/gateway for collecting and temporarily buffering
sensor data.

A central cloud platform provides the Smart City Operations
Dashboard, global monitoring, scheduling and resource-management
services.

The architecture combines the advantages of centralized
monitoring with decentralized data collection.

---

## 2. High-Level Architecture

```text
                    SMART CITY CLOUD
                 ┌─────────────────────┐
                 │ Operations Dashboard │
                 │                     │
                 │ SRTF Scheduler      │
                 │ Banker's Algorithm  │
                 │ Data Services       │
                 └──────────┬──────────┘
                            │
                    Secure Internet
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │  Zone-A  │   │  Zone-B  │   │  Zone-C  │
       │ Gateway  │   │ Gateway  │   │ Gateway  │
       └────┬─────┘   └────┬─────┘   └────┬─────┘
            │              │              │
       IoT Devices     IoT Devices    IoT Devices
            │              │              │
       ┌────┴─────┐   ┌────┴─────┐   ┌────┴─────┐
       │ Cameras  │   │ Cameras  │   │ Cameras  │
       │ Sensors  │   │ Sensors  │   │ Sensors  │
       │ Wearables│   │ Wearables│   │ Wearables│
       └──────────┘   └──────────┘   └──────────┘

# 3. Communication Plan

## A. Real-Time Public-Safety Alerts

Communication Type: Synchronous

Protocol: HTTPS over TCP

Flow:

IoT Device
    ↓
Zone Gateway
    ↓
HTTPS/TLS
    ↓
Cloud Dashboard/API
    ↓
Alert / Operator

Reason:

Public-safety alerts require reliable delivery and immediate
application-level acknowledgement. HTTPS over TCP provides
secure and reliable communication.

---

## B. Full-Day Sensor Logs

Communication Type: Asynchronous

Protocol: MQTT over TCP

Flow:

IoT Devices
    ↓
Zone Gateway
    ↓
MQTT Broker
    ↓
Cloud Storage

Reason:

Full-day sensor logs do not require immediate processing.
MQTT supports lightweight IoT communication and allows the
zone gateway to buffer and send data asynchronously.

# 4. Communication Summary

| Data Flow | Type | Protocol | Reason |
|---|---|---|---|
| Zone Gateway → Dashboard: Public-safety alerts | Synchronous | HTTPS/TCP | Reliable and immediate delivery |
| Zone Gateway → Cloud: Full-day sensor logs | Asynchronous | MQTT/TCP | Lightweight and supports buffering |
