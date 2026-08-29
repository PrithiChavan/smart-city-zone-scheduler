from jobs import JOBS


def calculate_metrics(start_time, finish_time, job):
    turnaround_time = finish_time - job["arrival_time"]
    waiting_time = turnaround_time - job["burst_time"]

    return {
        "start": start_time,
        "finish": finish_time,
        "waiting": waiting_time,
        "turnaround": turnaround_time
    }


def print_results(name, order, results):
    print("\n" + "=" * 65)
    print(name)
    print("=" * 65)

    print(
        f"{'Job ID':<10}"
        f"{'Start':<8}"
        f"{'Finish':<9}"
        f"{'Waiting':<10}"
        f"{'Turnaround':<12}"
    )

    for i in order:
        job = JOBS[i]
        result = results[i]

        print(
            f"{job['job_id']:<10}"
            f"{result['start']:<8}"
            f"{result['finish']:<9}"
            f"{result['waiting']:<10}"
            f"{result['turnaround']:<12}"
        )

    average_waiting = (
        sum(result["waiting"] for result in results.values())
        / len(JOBS)
    )

    average_turnaround = (
        sum(result["turnaround"] for result in results.values())
        / len(JOBS)
    )

    print("\nAverage waiting time   :", round(average_waiting, 3))
    print("Average turnaround time :", round(average_turnaround, 3))


# ---------------------------------------------------------
# FCFS — First Come, First Served
# ---------------------------------------------------------

def fcfs():
    current_time = 0
    remaining = set(range(len(JOBS)))

    order = []
    results = {}

    while remaining:

        ready = [
            i for i in remaining
            if JOBS[i]["arrival_time"] <= current_time
        ]

        if not ready:
            current_time = min(
                JOBS[i]["arrival_time"] for i in remaining
            )
            continue

        # Tie rule:
        # earlier arrival time, then lower job_id
        selected = min(
            ready,
            key=lambda i: (
                JOBS[i]["arrival_time"],
                JOBS[i]["job_id"]
            )
        )

        start_time = current_time
        current_time += JOBS[selected]["burst_time"]

        results[selected] = calculate_metrics(
            start_time,
            current_time,
            JOBS[selected]
        )

        order.append(selected)
        remaining.remove(selected)

    return order, results


# ---------------------------------------------------------
# Non-preemptive SJF — Shortest Job First
# ---------------------------------------------------------

def sjf():
    current_time = 0
    remaining = set(range(len(JOBS)))

    order = []
    results = {}

    while remaining:

        ready = [
            i for i in remaining
            if JOBS[i]["arrival_time"] <= current_time
        ]

        if not ready:
            current_time = min(
                JOBS[i]["arrival_time"] for i in remaining
            )
            continue

        # Choose shortest burst time.
        # Tie rule:
        # earlier arrival time, then lower job_id
        selected = min(
            ready,
            key=lambda i: (
                JOBS[i]["burst_time"],
                JOBS[i]["arrival_time"],
                JOBS[i]["job_id"]
            )
        )

        start_time = current_time
        current_time += JOBS[selected]["burst_time"]

        results[selected] = calculate_metrics(
            start_time,
            current_time,
            JOBS[selected]
        )

        order.append(selected)
        remaining.remove(selected)

    return order, results


# ---------------------------------------------------------
# SRTF — Shortest Remaining Time First
# ---------------------------------------------------------

def srtf():
    remaining_time = {
        i: JOBS[i]["burst_time"]
        for i in range(len(JOBS))
    }

    first_start = {}
    finish_time = {}

    timeline = []

    current_time = 0
    completed = 0

    while completed < len(JOBS):

        ready = [
            i for i in range(len(JOBS))
            if JOBS[i]["arrival_time"] <= current_time
            and remaining_time[i] > 0
        ]

        if not ready:
            current_time = min(
                JOBS[i]["arrival_time"]
                for i in range(len(JOBS))
                if remaining_time[i] > 0
            )
            continue

        # Choose job with shortest remaining time.
        # Tie rule:
        # earlier arrival time, then lower job_id
        selected = min(
            ready,
            key=lambda i: (
                remaining_time[i],
                JOBS[i]["arrival_time"],
                JOBS[i]["job_id"]
            )
        )

        if selected not in first_start:
            first_start[selected] = current_time

        # Run until either:
        # 1. The job finishes, or
        # 2. A new job arrives.
        future_arrivals = [
            JOBS[i]["arrival_time"]
            for i in range(len(JOBS))
            if remaining_time[i] > 0
            and JOBS[i]["arrival_time"] > current_time
        ]

        if future_arrivals:
            next_arrival = min(future_arrivals)
        else:
            next_arrival = current_time + remaining_time[selected]

        run_time = min(
            remaining_time[selected],
            next_arrival - current_time
        )

        start = current_time
        end = current_time + run_time

        timeline.append((start, end, selected))

        remaining_time[selected] -= run_time
        current_time = end

        if remaining_time[selected] == 0:
            finish_time[selected] = current_time
            completed += 1

    results = {}

    for i in range(len(JOBS)):

        turnaround_time = (
            finish_time[i] - JOBS[i]["arrival_time"]
        )

        waiting_time = (
            turnaround_time - JOBS[i]["burst_time"]
        )

        results[i] = {
            "start": first_start[i],
            "finish": finish_time[i],
            "waiting": waiting_time,
            "turnaround": turnaround_time
        }

    return timeline, results


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

if __name__ == "__main__":

    # FCFS
    fcfs_order, fcfs_results = fcfs()

    print_results(
        "FCFS — First Come, First Served",
        fcfs_order,
        fcfs_results
    )

    # SJF
    sjf_order, sjf_results = sjf()

    print_results(
        "Non-preemptive SJF — Shortest Job First",
        sjf_order,
        sjf_results
    )

    # SRTF
    srtf_timeline, srtf_results = srtf()

    srtf_order = list(range(len(JOBS)))

    print_results(
        "SRTF — Shortest Remaining Time First",
        srtf_order,
        srtf_results
    )

    print("\nSRTF execution timeline:")

    for start, end, job_index in srtf_timeline:
        print(
            f"{start} -> {end} : {JOBS[job_index]['job_id']}"
        )
