"""
Advent of code 2024 - Day 4 Part 1
"""

dummy_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def count_word(lines, pattern="XMAS"):
    """
    Count the occurences of XMAS: vertically, horizontally, diagonally, reverse, overlapping
    """
    rows = len(lines)
    cols = len(lines[0])
    first_letter = pattern[0]
    pattern_length = len(pattern)
    count = 0

    directions = [
        (0, 1),  # horizontal
        (1, 0),  # vertical
        (0, -1),  # horizontal reverse
        (-1, 0),  # vertical reverse
        (1, 1),  # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1),  # diagonal up-left
    ]

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != first_letter:
                continue

            for dr, dc in directions:
                match = True
                current_r = r
                current_c = c

                for k in range(pattern_length):
                    if not (0 <= current_r < rows and 0 <= current_c < cols):
                        # out of bounds
                        match = False
                        break

                    if lines[current_r][current_c] != pattern[k]:
                        match = False
                        break

                    current_r += dr
                    current_c += dc

                if match:
                    count += 1

    return count


if __name__ == "__main__":
    dummy_result = count_word(dummy_data)
    assert dummy_result == 18

    with open("./inputs/4.txt", "r") as f:
        input_data = f.read().strip().split("\n")
    result = count_word(input_data)
    print(f"Result: {result}")
