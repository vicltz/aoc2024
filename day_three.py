"""
Advent of code 2024 - Day 3 Part 1
"""

dummy_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def extract_mul_expressions(input_string):
    """
    1. check for mul(
    2. check that we have a closing parenthesis
    3. extract the content between the parentheses
    4. split by comma
    5. check that we have two integers
    """
    mul_expressions = []
    for i in range(len(input_string) - 4):
        if input_string[i : i + 4] == "mul(":
            # find the closing parenthesis
            closing_index = -1
            for j in range(i + 4, len(input_string)):
                if input_string[j] == ")":
                    closing_index = j
                    break
            if closing_index != -1:
                inside_parentheses = input_string[i + 4 : closing_index]
                parts = inside_parentheses.split(",")
                if len(parts) == 2:
                    try:
                        int1 = int(parts[0])
                        int2 = int(parts[1])
                        mul_expressions.append((int1, int2))
                    except ValueError:
                        continue

    return mul_expressions


def compute_mul_sum(input_string):
    mul_expressions = extract_mul_expressions(input_string)
    total_sum = 0
    for int1, int2 in mul_expressions:
        total_sum += int1 * int2
    return total_sum


if __name__ == "__main__":
    dummy_result = compute_mul_sum(dummy_data)
    assert dummy_result == 161
    with open("./inputs/3.txt", "r") as f:
        input_data = f.read().strip()
    result = compute_mul_sum(input_data)
    print(f"Result: {result}")
