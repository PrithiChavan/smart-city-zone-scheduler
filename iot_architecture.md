# Task 13 — IoT Connectivity and Architecture Layers

## 1. IoT Device and Connectivity Plan

The Smart City platform uses different communication
technologies depending on the device's bandwidth, range,
power consumption and use case.

| IoT Device | Communication Technology | Reason |
|---|---|---|
| Traffic-camera trigger | 5G | 5G provides high bandwidth and low latency, making it suitable for traffic events and camera-related data. |
| Environmental sensor | LoRaWAN | LoRaWAN provides long-range communication with very low power consumption, making it suitable for battery-powered environmental sensors. |
| Wearable public-safety device | NB-IoT | NB-IoT is designed for low-power, wide-area communication and is suitable for small, periodic safety telemetry from wearable devices. |

---

## 2. Traffic-Camera Trigger — 5G

A traffic-camera trigger uses **5G** because camera-related
events can require higher bandwidth and low latency.

5G is suitable for quickly transmitting traffic-event
information from an intersection to the zone gateway/cloud
platform.

---

## 3. Environmental Sensor — LoRaWAN

Environmental sensors may measure values such as air quality,
temperature and pollution levels.

**LoRaWAN** is suitable because these sensors usually send
small amounts of data and may operate on batteries for long
periods. Its long communication range and low power
requirements make it appropriate for city-wide environmental
monitoring.

---

## 4. Wearable Public-Safety Device — NB-IoT

A wearable public-safety device can periodically transmit
location/status or emergency telemetry.

**NB-IoT** is appropriate because it provides wide-area,
low-power connectivity for small amounts of telemetry and
supports long battery life.

---

# 5. IoT Architecture Layers

The Smart City platform is mapped to the six IoT architecture
layers as follows.

| IoT Architecture Layer | Smart City Platform Component |
|---|---|
| Physical Environment | Roads, traffic intersections, public areas and environmental locations |
| Perception/Device | Traffic cameras, environmental sensors and wearable public-safety devices |
| Gateway | Zone-A, Zone-B and Zone-C IoT gateways/controllers |
| Network Communication | 5G, LoRaWAN, NB-IoT, MQTT, HTTPS and TLS |
| Cloud Platform | Part 1's scheduler and Banker's-Algorithm engine |
| Application | Smart City Operations Dashboard and public-safety alert system |

---

## 6. Physical Environment Layer

The physical environment consists of the real-world locations
where the Smart City platform operates.

Examples include:

- Roads
- Traffic intersections
- Public areas
- Environmental monitoring locations
- Public-safety locations

These locations generate the physical conditions and events
that the IoT system monitors.

---

## 7. Perception/Device Layer

The Perception/Device Layer contains the devices that sense
or detect events.

Examples include:

- Traffic-camera triggers
- Environmental sensors
- Wearable public-safety devices

These devices collect information from the physical
environment.

---

## 8. Gateway Layer

Each zone contains a local IoT gateway/controller:

- Zone-A gateway/controller
- Zone-B gateway/controller
- Zone-C gateway/controller

The gateways collect data from IoT devices, perform initial
processing and buffering, and forward data to cloud services.

---

## 9. Network Communication Layer

The Network Communication Layer provides connectivity between
IoT devices, zone gateways and cloud services.

Technologies include:

- 5G
- LoRaWAN
- NB-IoT
- MQTT
- HTTPS
- TLS

These technologies provide the communication paths required
for sensor telemetry, alerts and archived sensor data.

---

## 10. Cloud Platform Layer

The Cloud Platform Layer contains **Part 1's scheduler and
Banker's-Algorithm engine**.

The scheduler processes zone-controller jobs using the
scheduling algorithms evaluated in Part 1, with SRTF selected
as the production scheduling choice for the measured workload.

The Banker's Algorithm performs deadlock-safety checks before
resource requests are granted.

---

## 11. Application Layer

The Application Layer contains the **Smart City Operations
Dashboard**.

The dashboard provides:

- Real-time public-safety alerts
- Sensor monitoring
- Zone status
- Scheduling information
- Resource-status information
- Operator controls and reports

The dashboard consumes processed data from the cloud platform.

---

# 12. Complete IoT Data Flow

```text
Physical Environment
        ↓
Perception / Devices
        ↓
Zone Gateway / Controller
        ↓
Network Communication
        ↓
Cloud Platform
(Part 1's Scheduler + Banker's Algorithm)
        ↓
Smart City Operations Dashboard
