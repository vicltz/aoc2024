"""
Advent of code 2024 - Day 4 Part 2
"""

from day_four import dummy_data


def count_xmas_diagonals(lines):
    """Count occurrences of X-MAS patterns (two MAS/SAM diagonals crossing)."""

    rows = len(lines)
    cols = len(lines[0])

    def is_sam_or_mas(a, b, c):
        return (a + b + c) in ["SAM", "MAS"]

    # keep a border of 1 to avoid boundary issues
    count = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if lines[r][c] != "A":
                continue

            diag_one = is_sam_or_mas(
                lines[r - 1][c - 1], lines[r][c], lines[r + 1][c + 1]
            )
            diag_two = is_sam_or_mas(
                lines[r - 1][c + 1], lines[r][c], lines[r + 1][c - 1]
            )

            if diag_one and diag_two:
                count += 1

    return count


if __name__ == "__main__":
    assert count_xmas_diagonals(dummy_data) == 9
    with open("./inputs/4.txt", "r") as f:
        input_data = f.read().strip().split("\n")
    result = count_xmas_diagonals(input_data)
    print(f"Result: {result}")
