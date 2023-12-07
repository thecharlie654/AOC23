# Part 1
# import re

# with open("day2.txt") as f:
#     lines = [line.strip() for line in f]

# split_lines = [re.split(":|;", line) for line in lines]

# def check_validity(game):
#     game.pop(0)
#     configuration_split = [configuration.split(",") for configuration in game]
#     for configuration in configuration_split:
#         for colour_count in configuration:
#             if "red" in colour_count:
#                 if int(colour_count[:-3]) > 12:
#                     return False
#             elif "green" in colour_count:
#                 if int(colour_count[:-5]) > 13:
#                     return False
#             elif "blue" in colour_count:
#                 if int(colour_count[:-4]) > 14:
#                     return False
#     return True

# valid_ids = []
# for game in split_lines:
#     id = int(game[0][5:])
#     if check_validity(game):
#         valid_ids.append(id)

# print(sum(valid_ids))

# Part 2
import re
import math

with open("day2.txt") as f:
    lines = [line.strip() for line in f]

split_lines = [re.split(":|;", line) for line in lines]

def find_greatest(game):
    red = []
    green = []
    blue = []
    game.pop(0)
    configuration_split = [configuration.split(",") for configuration in game]
    for configuration in configuration_split:
        for colour_count in configuration:
            if "red" in colour_count:
                red.append(int(colour_count[:-3]))
            elif "green" in colour_count:
                green.append(int(colour_count[:-5]))
            elif "blue" in colour_count:
                blue.append(int(colour_count[:-4]))
    greatest_red = sorted(red, reverse=True)[0]
    greatest_green = sorted(green, reverse=True)[0]
    greatest_blue = sorted(blue, reverse=True)[0]
    return [greatest_red, greatest_green, greatest_blue]

total = 0
for game in split_lines:
    id = int(game[0][5:])
    greatest = find_greatest(game)
    total += math.prod(greatest)

print(total)