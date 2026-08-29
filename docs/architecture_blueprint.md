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


# Task 10 — VPC-Based Network Boundary

## 1. VPC Design

The Smart City system will use **one VPC** containing three
dedicated private subnets, one for each zone.

```text
                    SMART CITY VPC
        ┌─────────────────────────────────────┐
        │                                     │
        │  ┌─────────────┐                    │
        │  │   Zone-A    │                    │
        │  │Private Subnet│                   │
        │  └─────────────┘                    │
        │                                     │
        │  ┌─────────────┐                    │
        │  │   Zone-B    │                    │
        │  │Private Subnet│                   │
        │  └─────────────┘                    │
        │                                     │
        │  ┌─────────────┐                    │
        │  │   Zone-C    │                    │
        │  │Private Subnet│                   │
        │  └─────────────┘                    │
        │                                     │
        │       Dashboard / Application       │
        │             Services                │
        │                                     │
        └─────────────────────────────────────┘
## 2. Subnet Structure

The VPC contains three dedicated private subnets:

- Zone-A private subnet
- Zone-B private subnet
- Zone-C private subnet

Each zone's IoT gateway/controller operates inside its
corresponding private subnet.

## 3. Network Isolation

The three private subnets provide logical separation between
Zone-A, Zone-B and Zone-C.

Resources in one zone should not be able to directly access
resources in another zone unless explicitly permitted.

## 4. Security Control

Security-group rules will enforce the network boundary.

For example, inbound traffic from the Zone-B subnet to
Zone-A resources will be denied.

Only explicitly approved communication between the zones
and the central dashboard/API will be allowed.

## 5. Final Design

The Smart City platform will use:

**One VPC + Three Dedicated Private Subnets**

This provides network isolation, controlled communication,
reduced attack surface and fault containment.

# Task 11 — Network Security Objectives

## 1. Protect Sensitive Data

**Control: Encryption at Rest (AES-256)**

Sensitive data such as sensor logs, the JOBS list and operational
records will be encrypted at rest using AES-256 encryption.
This prevents unauthorized users from reading stored data even
if the underlying storage is accessed.

---

## 2. Authentication

**Control: Mutual TLS (mTLS) with Device Certificates**

Zone controllers and IoT devices will use unique digital
certificates to authenticate themselves to the cloud platform.
This prevents unauthorized devices from connecting to the
Smart City system.

---

## 3. Authorization

**Control: IAM Least-Privilege Roles**

IAM roles will provide users and services only the permissions
required for their responsibilities. For example, a Zone
Operator can access assigned zone resources without receiving
administrative permissions.

---

## 4. Prevent Cyber Attacks

**Control: Web Application Firewall (WAF)**

A Web Application Firewall will inspect incoming application
traffic and block common attacks such as malicious requests,
injection attempts and other suspicious HTTP traffic.
This protects the Smart City Operations Dashboard and APIs.

---

## 5. Secure Communication

**Control: TLS 1.3**

All communication between zone controllers and cloud services
will use TLS 1.3. It encrypts data in transit and helps protect
public-safety alerts and sensor information from interception
or modification.

---

## 6. Ensure Availability

**Control: Multi-AZ Deployment with Health Checks**

The Smart City dashboard and critical cloud services will be
deployed across multiple availability zones with health checks.
If one instance or availability zone fails, another healthy
instance can continue serving the application.

---

# Security Control Summary

| Network-Security Objective | Specific Control |
|---|---|
| Protect sensitive data | AES-256 encryption at rest |
| Authentication | Mutual TLS (mTLS) with device certificates |
| Authorization | IAM least-privilege roles |
| Prevent cyber attacks | Web Application Firewall (WAF) |
| Secure communication | TLS 1.3 |
| Ensure availability | Multi-AZ deployment with health checks |

# Task 12 — IAM Table and Data-Protection Map

## 1. IAM Role Table

IAM (Identity and Access Management) is used to control who
can access Smart City resources and what actions they are
allowed to perform.

| Role | Specific Permissions |
|---|---|
| Zone Operator | Read sensor data and controller status for the assigned zone; acknowledge alerts; cannot modify IAM or network-security settings. |
| City Dashboard Admin | Read telemetry from all three zones; manage dashboard configuration and alert rules; cannot modify audit logs. |
| Auditor | Read-only access to audit logs, scheduling results and security events; cannot modify operational resources. |

---

## 2. Zone Operator

The Zone Operator has permissions limited to the assigned
zone.

Allowed:

- Read sensor telemetry
- Read zone-controller status
- Acknowledge public-safety alerts

Not allowed:

- Modify IAM roles
- Modify VPC/security-group rules
- Access unrelated zones

This follows the principle of least privilege.

---

## 3. City Dashboard Admin

The City Dashboard Admin manages the central Smart City
Operations Dashboard.

Allowed:

- Read telemetry from Zone-A, Zone-B and Zone-C
- Manage dashboard configuration
- Manage alert rules

The administrator does not receive permission to modify
audit records.

---

## 4. Auditor

The Auditor has read-only access.

Allowed:

- Read audit logs
- Read scheduling results
- Read security events

The Auditor cannot modify operational resources or system
configuration.

---

# 5. Data-Protection Map

The three required data states are:

1. At rest
2. In transit
3. In use

Each state is mapped to a specific protection technique and
a concrete example from this Smart City platform.

| Data State | Platform Example | Protection Technique |
|---|---|---|
| At rest | JOBS list and archived sensor logs stored on a zone controller/cloud storage | AES-256 encryption at rest |
| In transit | Public-safety alert sent from a zone controller to the Smart City Operations Dashboard | TLS 1.3 / HTTPS |
| In use | Banker's Algorithm safety check running in memory | Process isolation and least-privilege execution |

---

## 6. Data at Rest

### Example

The fixed `JOBS` list and archived sensor logs are stored on
zone-controller or cloud storage.

### Protection

**AES-256 encryption at rest** will protect the stored data.

Encryption ensures that stored information cannot be easily
read if unauthorized access to the storage occurs.

---

## 7. Data in Transit

### Example

A zone controller sends a real-time public-safety alert to
the Smart City Operations Dashboard.

### Protection

**TLS 1.3 over HTTPS** protects the communication.

TLS encrypts the data while it travels across the network and
helps prevent interception or modification.

---

## 8. Data in Use

### Example

The **Banker's Algorithm safety check from Part 1** runs in
memory while evaluating resource requests.

### Protection

**Process isolation and least-privilege execution** restrict
which processes can access the data while it is being processed.

The Banker's Algorithm service should run with only the
permissions required for its safety-check operation.

---

# 9. Principle of Least Privilege

Every role receives only the permissions necessary for its
job.

This reduces the impact of compromised accounts and prevents
unnecessary access to Smart City resources.

---

# 10. Summary

| Role / Data | Protection or Permission |
|---|---|
| Zone Operator | Limited access to assigned zone |
| City Dashboard Admin | Dashboard and alert management |
| Auditor | Read-only auditing |
| Data at rest | AES-256 encryption |
| Data in transit | TLS 1.3 / HTTPS |
| Data in use | Process isolation + least privilege |

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

# Task 14 — Threats and Mitigations

The Smart City platform uses IoT devices, zone controllers,
cloud services and a central Operations Dashboard. The following
threats are specifically relevant to this architecture.

## 1. Compromised IoT Device

### Threat

An attacker could compromise a traffic camera, environmental
sensor or wearable public-safety device and use it to send
false or malicious data to the Smart City platform.

False sensor data could result in incorrect alerts or poor
operational decisions.

### Mitigation

**Mutual TLS (mTLS) with unique device certificates** will
authenticate IoT devices before they are allowed to communicate
with the platform.

Compromised or revoked devices can have their certificates
revoked so they cannot continue accessing the system.

---

## 2. Denial-of-Service Attack

### Threat

An attacker could send a large number of requests to the
Smart City Operations Dashboard or its APIs.

This could consume cloud resources and prevent legitimate
operators from accessing public-safety information.

### Mitigation

**Web Application Firewall (WAF), rate limiting and DDoS
protection** will filter malicious traffic and limit excessive
requests.

The dashboard can also use multiple instances so that failure
of one instance does not make the entire service unavailable.

---

## 3. Unauthorized Cross-Zone Access

### Threat

An attacker who gains access to a Zone-B controller could
attempt to directly access Zone-A resources.

This could expose sensor data or allow unauthorized changes
to another zone.

### Mitigation

**VPC private subnets and security-group rules** will isolate
Zone-A, Zone-B and Zone-C.

Inbound traffic from the Zone-B subnet to Zone-A resources
will be denied unless explicitly required and permitted.

---

## 4. Data Interception

### Threat

An attacker could attempt to intercept public-safety alerts
or sensor information while it is travelling between a zone
controller and the cloud platform.

This could expose sensitive information or allow messages to
be modified.

### Mitigation

**TLS 1.3** will encrypt communication between zone controllers
and cloud services.

This protects data in transit from interception and
unauthorized modification.

---

## 5. Unauthorized Access to Stored Data

### Threat

An attacker who gains access to cloud storage or a zone
controller could attempt to read archived sensor logs or
operational information.

### Mitigation

**AES-256 encryption at rest with IAM-controlled key access**
will protect stored data.

Least-privilege IAM permissions will also ensure that only
authorized users and services can access the stored data.

---

# Threat and Mitigation Summary

| Threat | Specific Mitigation |
|---|---|
| Compromised IoT device | Mutual TLS (mTLS) and unique device certificates |
| Denial-of-Service attack | WAF, rate limiting and DDoS protection |
| Unauthorized cross-zone access | VPC private subnets and security-group rules |
| Data interception | TLS 1.3 |
| Unauthorized access to stored data | AES-256 encryption at rest + IAM |

---

# Final Security Approach

The Smart City platform will use multiple security layers:

1. Device authentication using mTLS certificates
2. VPC and subnet isolation
3. Security-group access controls
4. TLS 1.3 for communication
5. Encryption at rest
6. WAF and DDoS protection
7. Least-privilege IAM

These controls reduce the risk of compromised IoT devices,
unauthorized network access, data interception, data exposure
and availability attacks.
