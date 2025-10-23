"""
Advent of code 2024 - Day 2 Part 1
"""

import numpy as np


def split_levels_in_reports(input_data):
    reports = [level.split(" ") for level in input_data]
    return reports


def test_monotone(level_int):
    return level_int == sorted(level_int) or level_int == sorted(level_int, reverse=True)


def adjacent_differs_at_least_one(level_int):
    for i in range(len(level_int) - 1):
        if level_int[i] == level_int[i + 1]:
            return False
    return True


def adjacent_differs_max_three(level_int):
    for i in range(len(level_int) - 1):
        if abs(level_int[i] - level_int[i + 1]) > 3:
            return False
    return True


def test_safety(level):
    return (
        adjacent_differs_at_least_one(level)
        and adjacent_differs_max_three(level)
        and test_monotone(level)
    )


dummy_data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]

dummy_answers = [
    True,
    False,
    False,
    False,
    False,
    True
]

if __name__ == "__main__":
    # get input file:
    with open("./inputs/2.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    reports_dummy = split_levels_in_reports(dummy_data)
    
    for level, answer in zip(reports_dummy, dummy_answers):
        level_int = [int(i) for i in level]
        assert test_safety(level_int) == answer

    reports = split_levels_in_reports(input_data)

    sum_safe_levels = sum(test_safety([int(i) for i in level]) for level in reports)
    print(f"Solution (number of safe levels): {sum_safe_levels}")
