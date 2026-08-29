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
