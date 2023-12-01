import re

LEADING_NUM_PATTERN = re.compile("^[^\d]*(\d)")
TRAILING_NUM_PATTERN = re.compile(".*(\d)[^\d]*$")

sum = 0
with open("input.txt", "r") as file:
    for line in file:
        sum += int(
            LEADING_NUM_PATTERN.match(line).group(1)
            + TRAILING_NUM_PATTERN.match(line).group(1)
        )

print(f"Calibration value: {sum}")
