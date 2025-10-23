"""
Advent of code 2024 - Day 1 Part 2
"""

import numpy as np
from day_one import split_list
from day_one import dummy_data


def compute_similarity_score(input_data):
    left_list, right_list = split_list(input_data)
    score = 0
    for el in left_list:
        score += int(el)*right_list.count(el)
    return score

if __name__ == "__main__":

    with open('./inputs/1.txt', 'r') as f:
        input_data = f.read().strip().split('\n')

    assert compute_similarity_score(dummy_data) == 31
    solution = compute_similarity_score(input_data)

    print(f"Solution (similarity score): {solution}")