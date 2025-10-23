"""
Advent of code 2024 - Day 1 Part 1
"""

import numpy as np

dummy_data = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]


def split_list(input_data):
    left_list = []
    right_list = []
    for line in input_data:
        left, right = line.split("   ")
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list


def compute_total_distance(input_data):
    left_list, right_list = split_list(input_data)
    sort_left = sorted(left_list)
    sort_right = sorted(right_list)
    distance = np.abs(
        np.array(sort_left).astype(int) - np.array(sort_right).astype(int)
    )
    total_distance = np.sum(distance)
    return total_distance


if __name__ == "__main__":
    # get input file:
    with open("./inputs/1.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    assert compute_total_distance(dummy_data) == 11

    solution = compute_total_distance(input_data)

    print(f"Solution (total distance): {solution}")
