import threading
import time


# ---------------------------------------------------------
# Task 5 — Demonstrate the race condition
# ---------------------------------------------------------

def unsynchronized_run():
    """
    Demonstrates a race condition on a shared counter.

    Initial counter = 100
    Thread 1 subtracts 40
    Thread 2 adds 25

    Correct result = 85

    Both threads deliberately read the counter before either
    writes it, making a lost update observable.
    """

    counter = 100

    # Barrier forces both threads to finish their READ
    # before either thread performs its WRITE.
    read_barrier = threading.Barrier(2)

    def subtract_40():
        nonlocal counter

        old_value = counter

        read_barrier.wait()

        time.sleep(0.001)

        counter = old_value - 40

    def add_25():
        nonlocal counter

        old_value = counter

        read_barrier.wait()

        time.sleep(0.001)

        counter = old_value + 25

    thread1 = threading.Thread(
        target=subtract_40
    )

    thread2 = threading.Thread(
        target=add_25
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return counter


# ---------------------------------------------------------
# Peterson's Algorithm
# ---------------------------------------------------------

def peterson_run():
    """
    Protects the shared counter using Peterson's Algorithm.

    Peterson's Algorithm uses:
        flag[0]
        flag[1]
        turn

    to guarantee mutual exclusion between two threads.
    """

    counter = 100

    flag = [False, False]

    turn = 0

    def enter_critical_section(process):

        other = 1 - process

        flag[process] = True

        turn = other

        # Wait while the other process wants to enter
        # and it is the other process's turn.
        while flag[other] and turn == other:
            time.sleep(0)

    def leave_critical_section(process):

        flag[process] = False

    def subtract_40():
        nonlocal counter

        process = 0

        enter_critical_section(process)

        try:
            old_value = counter

            time.sleep(0.001)

            counter = old_value - 40

        finally:
            leave_critical_section(process)

    def add_25():
        nonlocal counter

        process = 1

        enter_critical_section(process)

        try:
            old_value = counter

            time.sleep(0.001)

            counter = old_value + 25

        finally:
            leave_critical_section(process)

    thread1 = threading.Thread(
        target=subtract_40
    )

    thread2 = threading.Thread(
        target=add_25
    )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return counter


# ---------------------------------------------------------
# Run the experiment
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 65)
    print("TASK 5 — PETERSON'S ALGORITHM")
    print("=" * 65)

    print("\nInitial counter value : 100")
    print("Thread 1 operation    : subtract 40")
    print("Thread 2 operation    : add 25")
    print("Correct final value   : 85")

    # ---------------------------------------------
    # Unsynchronized experiment — 5 runs
    # ---------------------------------------------

    print("\n" + "-" * 65)
    print("UNSYNCHRONIZED RUNS")
    print("-" * 65)

    unsynchronized_results = []

    for run_number in range(1, 6):

        result = unsynchronized_run()

        unsynchronized_results.append(result)

        print(
            f"Run {run_number}: final counter = {result}"
        )

    # ---------------------------------------------
    # Peterson's Algorithm — 5 runs
    # ---------------------------------------------

    print("\n" + "-" * 65)
    print("PETERSON'S ALGORITHM — PROTECTED RUNS")
    print("-" * 65)

    peterson_results = []

    for run_number in range(1, 6):

        result = peterson_run()

        peterson_results.append(result)

        print(
            f"Run {run_number}: final counter = {result}"
        )

    # ---------------------------------------------
    # Check acceptance criteria
    # ---------------------------------------------

    print("\n" + "=" * 65)
    print("RESULT")
    print("=" * 65)

    print(
        "\nUnsynchronized results:",
        unsynchronized_results
    )

    print(
        "Peterson results      :",
        peterson_results
    )

    incorrect_unsynchronized = any(
        value != 85
        for value in unsynchronized_results
    )

    all_peterson_correct = all(
        value == 85
        for value in peterson_results
    )

    print(
        "\nRace condition observed:",
        incorrect_unsynchronized
    )

    print(
        "Peterson correct on all 5 runs:",
        all_peterson_correct
    )

    if incorrect_unsynchronized and all_peterson_correct:
        print(
            "\nPASS: The unsynchronized version demonstrates "
            "a race condition, while Peterson's Algorithm "
            "protects the critical section and produces 85 "
            "on every run."
        )
    else:
        print(
            "\nPlease repeat the experiment."
        )
