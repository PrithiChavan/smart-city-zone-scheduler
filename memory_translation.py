# ============================================================
# TASK 7 — PAGING AND SEGMENTATION
# ============================================================


# ============================================================
# PART A — PAGING
# ============================================================

# Page size = 1024 bytes
PAGE_SIZE = 1024


# Page table:
# Page number -> Frame number

PAGE_TABLE = {
    0: 5,
    1: 2,
    2: 9,
    3: 1
}


def page_translate(logical_address):
    """
    Convert a logical address into a physical address.

    Logical address:
        page number + offset

    Physical address:
        frame number + offset
    """

    # Calculate page number
    page_number = logical_address // PAGE_SIZE

    # Calculate offset
    offset = logical_address % PAGE_SIZE

    # Check whether the page exists
    if page_number not in PAGE_TABLE:
        return "PAGE FAULT"

    # Get corresponding frame
    frame_number = PAGE_TABLE[page_number]

    # Calculate physical address
    physical_address = (
        frame_number * PAGE_SIZE
        + offset
    )

    return physical_address


# ============================================================
# PART B — SEGMENTATION
# ============================================================

# Segment table:
#
# Segment number -> (Base, Limit)

SEGMENT_TABLE = {
    0: (1000, 400),
    1: (2200, 300),
    2: (500, 150)
}


def segment_translate(segment_number, offset):
    """
    Convert a segmented logical address into a physical address.

    Valid condition:

        offset < limit

    Physical address:

        base + offset
    """

    # Check whether the segment exists
    if segment_number not in SEGMENT_TABLE:
        return "SEGMENTATION FAULT"

    base, limit = SEGMENT_TABLE[segment_number]

    # Check the offset against the segment limit
    if offset >= limit:
        return "SEGMENTATION FAULT"

    # Calculate physical address
    physical_address = base + offset

    return physical_address


# ============================================================
# DISPLAY PAGING TABLE
# ============================================================

def print_page_table():

    print("\n" + "=" * 60)
    print("PAGE TABLE")
    print("=" * 60)

    print(
        f"{'Page Number':<15}"
        f"{'Frame Number':<15}"
    )

    for page, frame in PAGE_TABLE.items():

        print(
            f"{page:<15}"
            f"{frame:<15}"
        )


# ============================================================
# DISPLAY SEGMENT TABLE
# ============================================================

def print_segment_table():

    print("\n" + "=" * 60)
    print("SEGMENT TABLE")
    print("=" * 60)

    print(
        f"{'Segment':<12}"
        f"{'Base':<12}"
        f"{'Limit':<12}"
    )

    for segment, values in SEGMENT_TABLE.items():

        base, limit = values

        print(
            f"{segment:<12}"
            f"{base:<12}"
            f"{limit:<12}"
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("TASK 7 — MEMORY ADDRESS TRANSLATION")
    print("=" * 60)

    print("\nPage size:", PAGE_SIZE, "bytes")

    # --------------------------------------------------------
    # PAGING
    # --------------------------------------------------------

    print_page_table()

    print("\n" + "-" * 60)
    print("PAGING ADDRESS TRANSLATION")
    print("-" * 60)

    logical_addresses = [
        260,
        1500,
        3000,
        5000
    ]

    for address in logical_addresses:

        result = page_translate(address)

        page = address // PAGE_SIZE
        offset = address % PAGE_SIZE

        print(
            f"Logical address {address}: "
            f"page={page}, "
            f"offset={offset} "
            f"-> {result}"
        )

    # --------------------------------------------------------
    # SEGMENTATION
    # --------------------------------------------------------

    print_segment_table()

    print("\n" + "-" * 60)
    print("SEGMENTATION ADDRESS TRANSLATION")
    print("-" * 60)

    segment_addresses = [
        (0, 150),
        (1, 350),
        (2, 100)
    ]

    for segment, offset in segment_addresses:

        result = segment_translate(
            segment,
            offset
        )

        print(
            f"Segment {segment}, "
            f"offset {offset} "
            f"-> {result}"
        )

    # --------------------------------------------------------
    # ACCEPTANCE SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("ACCEPTANCE SUMMARY")
    print("=" * 60)

    print("\nPaging:")

    print("260  ->", page_translate(260))
    print("1500 ->", page_translate(1500))
    print("3000 ->", page_translate(3000))
    print("5000 ->", page_translate(5000))

    print("\nSegmentation:")

    print(
        "(0, 150) ->",
        segment_translate(0, 150)
    )

    print(
        "(1, 350) ->",
        segment_translate(1, 350)
    )

    print(
        "(2, 100) ->",
        segment_translate(2, 100)
    )
