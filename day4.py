# Part 1
# import re
# with open("day4.txt") as f:
#     lines = [line for line in f]

# for i, line in enumerate(lines):
#     split_line = re.split(":|\|", line)
#     stripped_line = [sublist.strip() for sublist in split_line]
#     stripped_line.pop(0)
#     lines[i] = stripped_line

# card_values = []
# for card in lines:
#     winning_numbers = card[0].split(" ")
#     numbers_we_have = card[1].split(" ")
#     for i, item in enumerate(winning_numbers):
#         if item == "":
#             winning_numbers.pop(i)
#     for i, item in enumerate(numbers_we_have):
#         if item == "":
#             numbers_we_have.pop(i)
#     card_value = 0
#     for winning_number in winning_numbers:
#         if winning_number in numbers_we_have:
#             if card_value == 0:
#                 card_value += 1
#             else:
#                 card_value *= 2
#     card_values.append(card_value)

# print(sum(card_values))

# Part 2
import re
import time

with open("day4.txt") as f:
    lines = [line for line in f]

for i, line in enumerate(lines):
    split_line = re.split(":|\|", line)
    stripped_line = [sublist.strip() for sublist in split_line]
    lines[i] = stripped_line

def format_line_as_card(line):
    winning_numbers = line[1].split(" ")
    numbers_we_have = line[2].split(" ")
    for i, item in enumerate(winning_numbers):
        if item == "":
            winning_numbers.pop(i)
    for i, item in enumerate(numbers_we_have):
        if item == "":
            numbers_we_have.pop(i)
    return winning_numbers, numbers_we_have

def check_matches(winning_numbers, numbers_we_have):
    matches = 0
    for winning_number in winning_numbers:
        if winning_number in numbers_we_have:
            matches += 1
    return matches

def check_copies(copied_cards):
    global count
    for line in copied_cards:
        winning_numbers, numbers_we_have = format_line_as_card(line)
        matches = check_matches(winning_numbers, numbers_we_have)
        card_index = int(line[0][5:])
        copied_cards = []
        for j in range(matches):
            copied_cards.append(lines[card_index + j])
            count += 1
        check_copies(copied_cards)


card_values = []
global count
count = 0
for card_index, card in enumerate(lines):
    print(card_index)
    winning_numbers, numbers_we_have = format_line_as_card(card)
    matches = check_matches(winning_numbers, numbers_we_have)
    copied_cards = []
    for j in range(matches):
        copied_cards.append(lines[card_index + j + 1])
        count += 1
    check_copies(copied_cards)
    count += 1

print(count)