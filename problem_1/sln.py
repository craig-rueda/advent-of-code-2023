import re

NUM_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Build up a forward and reverse regex from our lookup table
LEADING_NUM_PATTERN = re.compile(f"({'|'.join(NUM_MAP.keys())}|\d)")
TRAILING_NUM_PATTERN = re.compile(
    f"({'|'.join([key[::-1] for key in NUM_MAP.keys()])}|\d)"
)


sum = 0
with open("input.txt", "r") as file:
    for line in file:
        # Chomp off trailing newline
        line = line.replace("\n", "")
        leading = LEADING_NUM_PATTERN.search(line).group()
        trailing = TRAILING_NUM_PATTERN.search(line[::-1]).group()

        # Convert val, if necessary
        leading = leading if len(leading) == 1 else NUM_MAP[leading]
        trailing = trailing if len(trailing) == 1 else NUM_MAP[trailing[::-1]]

        print(f"{line} -> {leading}{trailing}")
        sum += int(leading + trailing)

print(f"\nCalibration value: {sum}")
