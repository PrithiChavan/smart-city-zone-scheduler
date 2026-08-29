# Task 8 — Production Recommendation

## 1. Recommended Scheduling Policy

Based on the measured results from Tasks 2–4, the recommended
scheduling policy for production is:

**SRTF — Shortest Remaining Time First**

SRTF provides the lowest average waiting time and the lowest
average turnaround time for the given eight-job workload.

### Measured Results

| Scheduling Algorithm | Average Waiting Time | Average Turnaround Time |
|----------------------|----------------------|-------------------------|
| FCFS                 | 17.125               | 22.625                  |
| Non-preemptive SJF   | 13.000               | 18.500                  |
| SRTF                 | 11.500               | 17.000                  |
| Round Robin (q=3)    | 22.625               | 28.125                  |
| Round Robin (q=6)    | 20.375               | 25.875                  |
| Priority (no aging)  | 18.625               | 24.125                  |
| Priority (aging)     | 17.750               | 23.250                  |

Therefore:

**SRTF < SJF < FCFS**

for average waiting time on this workload.

---

## 2. Why SRTF is Recommended

SRTF is recommended because it gives priority to the process
with the shortest remaining execution time.

For this workload:

- Average waiting time is only **11.500**
- Average turnaround time is only **17.000**
- It performs better than FCFS and SJF.
- It also performs better than both tested Round Robin configurations.
- It provides good responsiveness for short jobs.

This makes SRTF suitable for a Smart City workload where short,
time-sensitive processing tasks may need to complete quickly.

---

## 3. Trade-offs

Although SRTF provides the best measured performance, it has
some disadvantages.

### Preemption overhead

SRTF may interrupt a running process when a new process arrives
with a shorter remaining time.

This can cause additional context switches and operating-system
overhead.

### Starvation

Long-running jobs can potentially wait for a long time if many
short jobs continuously arrive.

An aging mechanism or another fairness policy could be considered
if starvation becomes a problem in production.

### Additional information required

SRTF requires the scheduler to know or estimate the remaining
execution time of processes.

In a real operating system, execution-time estimates may not
always be accurate.

---

## 4. Comparison with Other Policies

### FCFS

FCFS is simple and easy to implement, but it produced a higher
average waiting time of **17.125**.

It can suffer from the convoy effect when a long job blocks
shorter jobs.

### Non-preemptive SJF

SJF improved the average waiting time to **13.000**.

However, unlike SRTF, SJF cannot preempt a currently running
process when a shorter job arrives.

### Round Robin

Round Robin is useful for fairness and interactive workloads.

For this workload:

- q=3 produced **16 context switches**
- q=6 produced **10 context switches**

The smaller quantum therefore creates more switching overhead.

### Priority Scheduling

Priority scheduling is useful when some processes are more
important than others.

However, without aging it can cause starvation of lower-priority
jobs.

Aging reduces this problem by gradually improving the effective
priority of jobs that have waited for a long time.

---

## 5. Final Production Decision

For the supplied eight-job workload, the production scheduler
should use:

**SRTF**

because it achieved:

- Lowest average waiting time: **11.500**
- Lowest average turnaround time: **17.000**

The other algorithms should remain available for testing,
benchmarking and workloads where fairness or fixed priorities
are more important than minimizing waiting time.

For a real deployment, SRTF should also be monitored for
starvation and context-switch overhead.

---

## 6. Deadlock Safety

The scheduling policy should be combined with the Banker's
Algorithm implemented in Task 6.

Before granting a resource request, the system should perform
the Banker's safety check.

For the supplied resource state:

- Initial state: **SAFE**
- Safe sequence: **p1 -> p3 -> p0 -> p2**
- P1 request `[1, 0, 2]`: **GRANT**
- P0 request `[2, 0, 2]`: **DENY**

Therefore, the production system should not grant a resource
request if it would make the system unsafe.

---

## 7. Overall Recommendation

The final Smart City processing system should therefore use:

1. **SRTF** for CPU scheduling for the supplied workload.
2. **Banker's Algorithm** for deadlock avoidance.
3. Monitoring of waiting time, turnaround time and context
   switches.
4. Additional fairness/starvation controls if the workload
   changes significantly.
