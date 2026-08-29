# Task 10 — VPC-Based Network Boundary

## 1. VPC Design

The Smart City system will use **one VPC** containing three dedicated
private subnets, one for each zone.

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
        │  │   Zone-B    │                   │
        │  │Private Subnet│                   │
        │  └─────────────┘                    │
        │                                     │
        │  ┌─────────────┐                    │
        │  │   Zone-C    │                   │
        │  │Private Subnet│                   │
        │  └─────────────┘                    │
        │                                     │
        │       Dashboard / Application       │
        │             Services                │
        │                                     │
        └─────────────────────────────────────┘
2. Subnet Structure
The VPC contains three dedicated private subnets:
Zone-A private subnet
Zone-B private subnet
Zone-C private subnet
Each zone's IoT gateway/controller operates inside its corresponding private subnet.
3. Logical Isolation and Customizability
The three private subnets provide logical isolation between Zone-A, Zone-B and Zone-C. Resources in one zone cannot directly access resources in another zone unless communication is explicitly permitted.
The VPC also provides customizability because separate routing, network ACL and security policies can be applied to each subnet according to the security requirements of each zone.
4. Specific Network-Level Security Control
A Network ACL (NACL) will be applied to the Zone-A private subnet with an explicit DENY rule for inbound traffic from the Zone-B subnet CIDR.
This network-level rule prevents Zone-B resources from directly reaching Zone-A resources. Only explicitly approved communication, such as permitted traffic to the central dashboard/API, will be allowed.
The Smart City Operations Dashboard is an application that consumes data after network access has already been permitted; it is not the control enforcing the Zone-A/Zone-B boundary.
5. Final Design
The Smart City platform will use:
One VPC + Three Dedicated Private Subnets
This design provides logical isolation, customizable network policies, controlled communication, reduced attack surface and fault containment.
