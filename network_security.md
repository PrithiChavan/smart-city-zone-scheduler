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
