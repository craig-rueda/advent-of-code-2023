matrix = []
num_sum = 0


def find_adjacent_spec_char(x: int, y: int) -> str:
    # Grab adjacent Rows
    prev_row = matrix[y - 1 if y != 0 else 0]
    curr_row = matrix[y]
    next_row = matrix[y + 1 if y < len(matrix) - 1 else y]

    # Grab right/left adjacent
    left_idx = x - 1 if x else x
    right_idx = x + 1 if x < len(curr_row) - 1 else x

    adjacent_chars = (
        prev_row[left_idx : right_idx + 1]
        + [curr_row[left_idx], curr_row[right_idx]]
        + next_row[left_idx : right_idx + 1]
    )

    return any([is_special_char(character) for character in adjacent_chars])


def is_special_char(character: str) -> bool:
    return character != "." and not character.isnumeric()


# Populate the matrix
with open("input.txt", "r") as file:
    for line in file:
        matrix.append(list(line))

# Iterate over each line, checking neghbors along the way
for row_idx in range(0, len(matrix)):
    row = matrix[row_idx]
    current_num = ""
    has_adjacent_spec_char = False
    included_nums = []
    excluded_nums = []

    for col_idx in range(0, len(row)):
        curr_char = row[col_idx]
        is_num_char = curr_char.isnumeric()

        if is_num_char:
            current_num += curr_char
            has_adjacent_spec_char = has_adjacent_spec_char or find_adjacent_spec_char(
                col_idx, row_idx
            )

        if not is_num_char or col_idx == len(row) - 1:
            if current_num and has_adjacent_spec_char:
                num_sum += int(current_num)
                included_nums.append(current_num)
            elif current_num:
                excluded_nums.append(current_num)

            current_num = ""
            has_adjacent_spec_char = False

    print(f"{row_idx + 1} inc:{included_nums} exc:{excluded_nums}")


print(f"Final sum: {num_sum}")
