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
