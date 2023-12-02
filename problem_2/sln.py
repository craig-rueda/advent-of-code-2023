from math import prod
import re

GAME_ID_PATTERN = re.compile("Game (\d+):(.*)")
GAME_COLOR_PATTERN = re.compile("(\d+) (blue|red|green)")


#
# Rules defined in problem spec
#
def check_possible(color: str, cnt: int) -> bool:
    return (
        (color == "red" and cnt <= 12)
        or (color == "green" and cnt <= 13)
        or (color == "blue" and cnt <= 14)
    )


id_sum = 0
power_sum = 0
with open("input.txt", "r") as file:
    #
    # For each line, pull out the game ID, then split each remainder
    # on ';' in order to pull out the runs. For each run, match the
    # color and their cnts in order to process further
    #
    for line in file:
        m = GAME_ID_PATTERN.match(line)
        game_id = int(m.group(1))
        game_runs = m.group(2).split(";")

        is_possible = True
        min_possible = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for run in game_runs:
            for color_draw in GAME_COLOR_PATTERN.findall(run):
                color_cnt, color_name = color_draw
                color_cnt_int = int(color_cnt)
                is_possible = check_possible(color_name, color_cnt_int) and is_possible
                min_possible[color_name] = max(min_possible[color_name], color_cnt_int)

        if is_possible:
            id_sum += game_id

        game_power = prod(min_possible.values())
        power_sum += game_power

        # Print each line as we go to smoke check
        print(f"{game_id} -> Possible: {is_possible} / Power: {game_power}")

# Print final result
print(f"\nGame_ID sum: {id_sum} / Power Sum: {power_sum}")
