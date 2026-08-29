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
