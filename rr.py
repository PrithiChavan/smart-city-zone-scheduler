from collections import deque
from jobs import JOBS


def round_robin(quantum):
    remaining_time = {
        i: JOBS[i]["burst_time"]
        for i in range(len(JOBS))
    }

    first_start = {}
    finish_time = {}

    arrived = set()
    ready_queue = deque()

    timeline = []

    current_time = 0

    def add_arrivals(time):
        for i, job in enumerate(JOBS):
            if (
                i not in arrived
                and job["arrival_time"] <= time
            ):
                ready_queue.append(i)
                arrived.add(i)

    # Add jobs that have arrived at time 0
    add_arrivals(current_time)

    while len(finish_time) < len(JOBS):

        # If queue is empty, move time to the next arrival
        if not ready_queue:
            next_time = min(
                JOBS[i]["arrival_time"]
                for i in range(len(JOBS))
                if i not in arrived
            )

            current_time = next_time
            add_arrivals(current_time)

        selected = ready_queue.popleft()

        # Record the first time this job starts
        if selected not in first_start:
            first_start[selected] = current_time

        start_time = current_time

        # Run for one quantum or until the job finishes
        run_time = min(
            quantum,
            remaining_time[selected]
        )

        current_time += run_time

        remaining_time[selected] -= run_time

        timeline.append(
            (
                start_time,
                current_time,
                selected
            )
        )

        # IMPORTANT:
        # If a new job arrives exactly when the quantum expires,
        # add the new job BEFORE re-adding the expired job.
        add_arrivals(current_time)

        # If the selected job is not finished,
        # put it at the back of the queue.
        if remaining_time[selected] > 0:
            ready_queue.append(selected)
        else:
            finish_time[selected] = current_time

    # Calculate waiting and turnaround time
    results = {}

    for i in range(len(JOBS)):

        turnaround_time = (
            finish_time[i]
            - JOBS[i]["arrival_time"]
        )

        waiting_time = (
            turnaround_time
            - JOBS[i]["burst_time"]
        )

        results[i] = {
            "start": first_start[i],
            "finish": finish_time[i],
            "waiting": waiting_time,
            "turnaround": turnaround_time
        }

    # Context switches = changes from one job to another
    context_switches = 0

    for previous, current in zip(
        timeline,
        timeline[1:]
    ):
        if previous[2] != current[2]:
            context_switches += 1

    return timeline, results, context_switches


def print_results(quantum, timeline, results, switches):

    print("\n" + "=" * 65)
    print(f"ROUND ROBIN — TIME QUANTUM = {quantum}")
    print("=" * 65)

    print(
        f"{'Job ID':<10}"
        f"{'Start':<8}"
        f"{'Finish':<9}"
        f"{'Waiting':<10}"
        f"{'Turnaround':<12}"
    )

    for i in range(len(JOBS)):

        result = results[i]

        print(
            f"{JOBS[i]['job_id']:<10}"
            f"{result['start']:<8}"
            f"{result['finish']:<9}"
            f"{result['waiting']:<10}"
            f"{result['turnaround']:<12}"
        )

    average_waiting = (
        sum(
            result["waiting"]
            for result in results.values()
        )
        / len(JOBS)
    )

    average_turnaround = (
        sum(
            result["turnaround"]
            for result in results.values()
        )
        / len(JOBS)
    )

    print("\nAverage waiting time   :", round(average_waiting, 3))
    print(
        "Average turnaround time :",
        round(average_turnaround, 3)
    )

    print("Context switches       :", switches)

    print("\nExecution timeline:")

    for start, finish, job_index in timeline:
        print(
            f"{start} -> {finish} : "
            f"{JOBS[job_index]['job_id']}"
        )


if __name__ == "__main__":

    # -----------------------------------------
    # Round Robin with quantum = 3
    # -----------------------------------------

    timeline_3, results_3, switches_3 = round_robin(3)

    print_results(
        3,
        timeline_3,
        results_3,
        switches_3
    )

    # -----------------------------------------
    # Round Robin with quantum = 6
    # -----------------------------------------

    timeline_6, results_6, switches_6 = round_robin(6)

    print_results(
        6,
        timeline_6,
        results_6,
        switches_6
    )

    # -----------------------------------------
    # Comparison
    # -----------------------------------------

    print("\n" + "=" * 65)
    print("ROUND ROBIN COMPARISON")
    print("=" * 65)

    print(
        "Quantum 3 context switches:",
        switches_3
    )

    print(
        "Quantum 6 context switches:",
        switches_6
    )

    print(
        "\nTheory statement:"
    )

    print(
        "A smaller quantum causes more context-switch "
        "overhead because jobs are switched more frequently. "
        "For this workload, quantum 3 has more switches "
        f"({switches_3}) than quantum 6 ({switches_6}), "
        "so a real OS would incur more switching overhead "
        "with quantum 3."
    )
