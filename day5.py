# Part 1
with open("day5.txt") as f:
    lines = [line.strip() for line in f]

seeds = list(map(int, lines[0][7:].split(" ")))

maps = []
submap = []
for line in lines:
    try:
        int(line[0])
        submap.append(list(map(int, line.split(" "))))
    except ValueError:
        if submap != []:
            maps.append(submap)
        submap = []
    except IndexError:
        pass
maps.append(submap)

for seed_index, seed in enumerate(seeds):
    # print(f"STARTING SEED {seed}")
    for submap in maps:
        for subsubmap in submap:
            dest_pos = None
            dest_start = subsubmap[0]
            source_start = subsubmap[1]
            range_len = subsubmap[2]
            if (source_start + range_len) - seed <= range_len and (source_start + range_len) - seed >= 0:
                # print(f"Seed is between {source_start} and {source_start + range_len}")
                dest_pos = dest_start + (seed - source_start)
                seeds[seed_index] = dest_pos
                seed = dest_pos
                # print(f"Seed is now {seed}")
                break
        # if dest_pos is None:
            # print(f"Seed is not in ranges, maintaining value {seed}")
    # print("")

print(min(seeds))