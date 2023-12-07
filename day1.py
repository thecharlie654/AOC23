# Part 1
# with open("day1.txt") as f:
#     all_line_digits = []
#     for line in f:
#         line_digits = []
#         for char in [*line]:
#             try:
#                 int(char)
#                 line_digits.append(char)
#             except ValueError:
#                 pass
#         all_line_digits.append(line_digits)

# first_last_digits = [[line[0], line[-1:][0]] for line in all_line_digits]

# total_sum = 0
# for line in first_last_digits:
#     total_sum += int("".join(line))

# print(total_sum)

# Part 2
import time
import random

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def check_line_for_number_word(line, delete_line_number_words):
    if delete_line_number_words is True:
        global line_number_words
        line_number_words = []
    for word in number_words:
        if word in line:
            number_word_pos = line.index(word)
            line_split = [*line]
            if number_word_pos not in [sublist[0] for sublist in line_number_words]:
                line_number_words.append([number_word_pos, word])
            line_split_modified = line_split
            for i in range(len(word)):
                line_split_modified[number_word_pos + i] = "#"
            check_line_for_number_word("".join(line_split_modified), False)
    return [[sublist[0], number_words.index(sublist[1]) + 1] for sublist in line_number_words]

def check_line_for_number_digits(line):
    line_number_digits = []
    split_line = [*line]
    for i, char in enumerate(split_line):
        try:
            int(char)
            line_number_digits.append([i, int(char)])
        except ValueError:
            pass
    return line_number_digits

with open("day1.txt") as f:
    all_lines = [line for line in f]

all_line_digits = []
for line in all_lines:
    line_number_words = check_line_for_number_word(line, True)
    line_number_digits = check_line_for_number_digits(line)
    for sublist in line_number_digits:
        line_number_words.append(sublist)
    line_number_words.sort(key = lambda sublist: sublist[0])
    line_digits = [sublist[1] for sublist in line_number_words]
    all_line_digits.append(line_digits)

first_last_digits = [[line[0], line[-1:][0]] for line in all_line_digits]

total_sum = 0
for line in first_last_digits:
    total_sum += int("".join([str(char) for char in line]))

print(total_sum)