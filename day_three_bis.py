"""
Advent of code 2024 - Day 3 Part 2
"""

from day_three import compute_mul_sum

dummy_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def preprocess_input(input_string):
    """
    Remove all parts of the string that are between "don't()" and the next "do()"
    """
    input_string_list = list(input_string)
    useless_indices = []
    allowed_state = True
    for i in range(len(input_string) - 7):
        if input_string[i : i + 4] == "do()":
            allowed_state = True
        elif input_string[i : i + 7] == "don't()":
            allowed_state = False

        if not allowed_state:
            # remove elements until next state change
            useless_indices.append(i)

    for index in sorted(useless_indices, reverse=True):
        input_string_list.pop(index)

    return "".join(input_string_list)


if __name__ == "__main__":
    dummy_result = compute_mul_sum(preprocess_input(dummy_data))
    assert dummy_result == 48

    with open("./inputs/3.txt", "r") as f:
        input_data = f.read().strip()
    result = compute_mul_sum(preprocess_input(input_data))
    print(f"Result: {result}")
