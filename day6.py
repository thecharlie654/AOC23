# Part 1
# import math

# with open("day6.txt") as f:
#     lines = [line.strip() for line in f]

# times = lines[0].split(" ")
# times = [int(item) for item in times if item.isdigit()]

# distances = lines[1].split(" ")
# distances = [int(item) for item in distances if item.isdigit()]

# all_record_beating_times = []
# for time_index, time in enumerate(times):
#     race_record_beating_times = 0
#     for button_held_duration in range(time + 1):
#         time_remaining = time - button_held_duration
#         distance = button_held_duration * time_remaining
#         record = distances[time_index]
#         if distance > record:
#             race_record_beating_times += 1
#     all_record_beating_times.append(race_record_beating_times)

# print(math.prod(all_record_beating_times))

# Part 2
with open("day6.txt") as f:
    lines = [line.strip() for line in f]

times = lines[0].split(" ")
times = [item for item in times if item.isdigit()]
time = int("".join(times))

distances = lines[1].split(" ")
distances = [item for item in distances if item.isdigit()]
distance = int("".join(distances))


race_record_beating_times = 0
for button_held_duration in range(time + 1):
    time_remaining = time - button_held_duration
    current_distance = button_held_duration * time_remaining
    record = distance
    if current_distance > record:
        race_record_beating_times += 1

print(race_record_beating_times)