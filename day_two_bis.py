"""
Advent of code 2024 - Day 2 Part 2
"""
from day_two import split_levels_in_reports, test_safety, dummy_data

updated_dummy_answers = [
    True,
    False,
    False,
    True,
    True,
    True
]

def test_updated_safety(level_int):
    if test_safety(level_int):
        return True
    # sublevels , ie sublist with one element removed       
    for i in range(len(level_int)):
        sub_level = level_int.copy()
        sub_level.pop(i)
        if test_safety(sub_level):
            return True
    return False

if __name__ == "__main__":
    # get input file:
    with open("./inputs/2.txt", "r") as f:
        input_data = f.read().strip().split("\n")

    reports_dummy = split_levels_in_reports(dummy_data)
    
    for level, answer in zip(reports_dummy, updated_dummy_answers):
        level_int = [int(i) for i in level]
        assert test_updated_safety(level_int) == answer

    reports = split_levels_in_reports(input_data)

    sum_safe_levels = sum(test_updated_safety([int(i) for i in level]) for level in reports)
    print(f"Solution (number of safe levels): {sum_safe_levels}")
