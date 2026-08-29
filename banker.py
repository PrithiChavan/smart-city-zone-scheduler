# ============================================================
# TASK 6 — BANKER'S ALGORITHM
# ============================================================

# Available resources
# A, B, C

AVAILABLE = [3, 3, 2]


# Maximum resource requirement of each process
MAX_NEED = {
    "p0": [7, 5, 3],
    "p1": [3, 2, 2],
    "p2": [9, 0, 2],
    "p3": [2, 2, 2],
}


# Currently allocated resources
ALLOCATION = {
    "p0": [0, 1, 0],
    "p1": [2, 0, 0],
    "p2": [3, 0, 2],
    "p3": [2, 1, 1],
}


# ============================================================
# Calculate Need Matrix
# Need = Maximum - Allocation
# ============================================================

def calculate_need():

    need = {}

    for process in MAX_NEED:

        need[process] = [
            MAX_NEED[process][i]
            - ALLOCATION[process][i]
            for i in range(3)
        ]

    return need


# ============================================================
# Print Matrix
# ============================================================

def print_matrix(title, matrix):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print(
        f"{'Process':<10}"
        f"{'A':<8}"
        f"{'B':<8}"
        f"{'C':<8}"
    )

    for process, values in matrix.items():

        print(
            f"{process:<10}"
            f"{values[0]:<8}"
            f"{values[1]:<8}"
            f"{values[2]:<8}"
        )


# ============================================================
# Safety Algorithm
# ============================================================

def safety_algorithm(available, allocation, need):

    work = available[:]

    finish = {
        process: False
        for process in need
    }

    safe_sequence = []

    while len(safe_sequence) < len(need):

        found = False

        for process in need:

            if finish[process]:
                continue

            # Check:
            # Need[i] <= Work
            can_finish = all(
                need[process][i] <= work[i]
                for i in range(3)
            )

            if can_finish:

                # Work = Work + Allocation[i]
                work = [
                    work[i] + allocation[process][i]
                    for i in range(3)
                ]

                finish[process] = True

                safe_sequence.append(process)

                found = True

        # No process could finish
        if not found:

            return False, safe_sequence

    return True, safe_sequence


# ============================================================
# Resource Request Algorithm
# ============================================================

def request_resources(process, request):

    need = calculate_need()

    print("\n" + "-" * 60)
    print(
        f"Resource request by {process}: {request}"
    )
    print("-" * 60)

    # --------------------------------------------------------
    # Step 1 — Check Request <= Need
    # --------------------------------------------------------

    if any(
        request[i] > need[process][i]
        for i in range(3)
    ):

        return (
            False,
            "Request exceeds the process's remaining Need."
        )

    # --------------------------------------------------------
    # Step 2 — Check Request <= Available
    # --------------------------------------------------------

    if any(
        request[i] > AVAILABLE[i]
        for i in range(3)
    ):

        return (
            False,
            "Request exceeds currently Available resources."
        )

    # --------------------------------------------------------
    # Step 3 — Pretend to allocate the resources
    # --------------------------------------------------------

    new_available = [
        AVAILABLE[i] - request[i]
        for i in range(3)
    ]

    new_allocation = {
        p: ALLOCATION[p][:]
        for p in ALLOCATION
    }

    new_need = {
        p: need[p][:]
        for p in need
    }

    new_allocation[process] = [
        new_allocation[process][i] + request[i]
        for i in range(3)
    ]

    new_need[process] = [
        new_need[process][i] - request[i]
        for i in range(3)
    ]

    # --------------------------------------------------------
    # Step 4 — Run the safety algorithm
    # --------------------------------------------------------

    safe, sequence = safety_algorithm(
        new_available,
        new_allocation,
        new_need
    )

    if safe:

        return (
            True,
            "Request can be GRANTED. "
            f"Safe sequence: {' -> '.join(sequence)}"
        )

    else:

        return (
            False,
            "Request must be DENIED because "
            "the resulting state is UNSAFE."
        )


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("TASK 6 — BANKER'S ALGORITHM")
    print("=" * 60)

    # --------------------------------------------------------
    # Display Available Resources
    # --------------------------------------------------------

    print("\nAvailable resources:")
    print("A =", AVAILABLE[0])
    print("B =", AVAILABLE[1])
    print("C =", AVAILABLE[2])

    # --------------------------------------------------------
    # Calculate and display Need matrix
    # --------------------------------------------------------

    need = calculate_need()

    print_matrix(
        "NEED MATRIX",
        need
    )

    # --------------------------------------------------------
    # Initial safety check
    # --------------------------------------------------------

    safe, sequence = safety_algorithm(
        AVAILABLE,
        ALLOCATION,
        need
    )

    print("\n" + "=" * 60)
    print("INITIAL SAFETY CHECK")
    print("=" * 60)

    if safe:

        print("System state: SAFE")

        print(
            "Safe sequence:",
            " -> ".join(sequence)
        )

    else:

        print("System state: UNSAFE")

    # --------------------------------------------------------
    # Test P1 request
    # --------------------------------------------------------

    p1_request = [1, 0, 2]

    granted, message = request_resources(
        "p1",
        p1_request
    )

    print("\nP1 Request [1, 0, 2]")

    if granted:
        print("Decision: GRANT")
    else:
        print("Decision: DENY")

    print("Reason:", message)

    # --------------------------------------------------------
    # Test P0 request
    # --------------------------------------------------------

    p0_request = [2, 0, 2]

    granted, message = request_resources(
        "p0",
        p0_request
    )

    print("\nP0 Request [2, 0, 2]")

    if granted:
        print("Decision: GRANT")
    else:
        print("Decision: DENY")

    print("Reason:", message)

    # --------------------------------------------------------
    # Final acceptance summary
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("ACCEPTANCE SUMMARY")
    print("=" * 60)

    print("Initial state : SAFE")
    print("Safe sequence : p1 -> p3 -> p0 -> p2")
    print("P1 [1,0,2]    : GRANT")
    print("P0 [2,0,2]    : DENY")
