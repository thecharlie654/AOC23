# Part 1

# with open("day3.txt") as f:
#     lines = [line.strip() for line in f]

# def search_around_symbol(line_no, char_no):
#     try: int(lines[line_no - 1][char_no]); found_ints.append([line_no - 1, char_no])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no + 1][char_no]); found_ints.append([line_no + 1, char_no])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no][char_no - 1]); found_ints.append([line_no, char_no - 1])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no][char_no + 1]); found_ints.append([line_no, char_no + 1])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no - 1][char_no - 1]); found_ints.append([line_no - 1, char_no - 1])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no - 1][char_no + 1]); found_ints.append([line_no - 1, char_no + 1])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no + 1][char_no - 1]); found_ints.append([line_no + 1, char_no - 1])
#     except (ValueError, IndexError): pass
#     try: int(lines[line_no + 1][char_no + 1]); found_ints.append([line_no + 1, char_no + 1])
#     except (ValueError, IndexError): pass

# def int_search_along_row():
#     try:
#         i = 0
#         loop = True
#         while loop:
#             if [integer_position[0], integer_position[1] - i] in full_integer_positions:
#                 loop = False
#             else:
#                 full_integer.insert(0, int(lines[integer_position[0]][integer_position[1] - i]))
#                 full_integer_positions.append([integer_position[0], integer_position[1] - i])
#                 i += 1
#     except Exception as e:
#         pass

#     try:
#         i = 1
#         loop = True
#         while loop:
#             if [integer_position[0], integer_position[1] + i] in full_integer_positions:
#                 loop = False
#             else:
#                 full_integer.append(int(lines[integer_position[0]][integer_position[1] + i]))
#                 full_integer_positions.append([integer_position[0], integer_position[1] + i])
#                 i += 1
#     except Exception as e:
#         pass

# found_ints = []
# for line_no, line in enumerate(lines):
#     for char_no, char in enumerate(line):
#         try:
#             int(char)
#         except ValueError:
#             if char == ".":
#                 continue
#             else:
#                 search_around_symbol(line_no, char_no)

# full_integer_positions = []
# integers = []
# for integer_position in found_ints:
#     full_integer = []
#     int_search_along_row()
#     if full_integer != []:
#         integers.append("".join([str(digit) for digit in full_integer]))

# integers = [int(integer) for integer in integers]
# print(sum(integers))

# Part 2
with open("day3.txt") as f:
    lines = [line.strip() for line in f]

def search_around_symbol(line_no, char_no):
    try: int(lines[line_no - 1][char_no]); found_ints.append([line_no - 1, char_no])
    except (ValueError, IndexError): pass
    try: int(lines[line_no + 1][char_no]); found_ints.append([line_no + 1, char_no])
    except (ValueError, IndexError): pass
    try: int(lines[line_no][char_no - 1]); found_ints.append([line_no, char_no - 1])
    except (ValueError, IndexError): pass
    try: int(lines[line_no][char_no + 1]); found_ints.append([line_no, char_no + 1])
    except (ValueError, IndexError): pass
    try: int(lines[line_no - 1][char_no - 1]); found_ints.append([line_no - 1, char_no - 1])
    except (ValueError, IndexError): pass
    try: int(lines[line_no - 1][char_no + 1]); found_ints.append([line_no - 1, char_no + 1])
    except (ValueError, IndexError): pass
    try: int(lines[line_no + 1][char_no - 1]); found_ints.append([line_no + 1, char_no - 1])
    except (ValueError, IndexError): pass
    try: int(lines[line_no + 1][char_no + 1]); found_ints.append([line_no + 1, char_no + 1])
    except (ValueError, IndexError): pass

def int_search_along_row():
    try:
        i = 0
        loop = True
        while loop:
            if [integer_position[0], integer_position[1] - i] in full_integer_positions:
                loop = False
            else:
                full_integer.insert(0, int(lines[integer_position[0]][integer_position[1] - i]))
                full_integer_positions.append([integer_position[0], integer_position[1] - i])
                i += 1
    except Exception as e:
        pass

    try:
        i = 1
        loop = True
        while loop:
            if [integer_position[0], integer_position[1] + i] in full_integer_positions:
                loop = False
            else:
                full_integer.append(int(lines[integer_position[0]][integer_position[1] + i]))
                full_integer_positions.append([integer_position[0], integer_position[1] + i])
                i += 1
    except Exception as e:
        pass

all_ints = []
for line_no, line in enumerate(lines):
    for char_no, char in enumerate(line):
        if char == "*":
            found_ints = []
            search_around_symbol(line_no, char_no)
            all_ints.append(found_ints)

full_integer_positions = []
integers = []
for symbol in all_ints:
    symbol_surrounding_ints = []
    for position_around_symbol in symbol:
        full_integer = []
        integer_position = position_around_symbol
        int_search_along_row()
        if full_integer != []:
            symbol_surrounding_ints.append("".join([str(digit) for digit in full_integer]))
    integers.append([int(integer) for integer in symbol_surrounding_ints])

total = 0
for integer_list in integers:
    if len(integer_list) == 2:
        total += (integer_list[0] * integer_list[1])

print(total)