test = open('input5.txt', 'r')
test = test.read().split('\n\n')

seeds = [int(x) for x in test[0].split(' ')[1:]]
current_set = seeds.copy()
lowest = 0

#####Part 1 with Dictionary

# for mapping_lines in test[1:]:
#     Mapping={}
#     for line in mapping_lines.split("\n"):
#         if line!="" and line[0].isnumeric():
#             d, s, x = [int(x) for x in line.split(' ')]
#             dest = [i for i in range(d, d+x)]
#             source = [i for i in range(s, s+x)]
#             Mapping.update(dict(map(lambda i,j : (i,j) , source, dest)))
#     for i in range(len(current_set)):
#         if current_set[i] in Mapping.keys():
#             current_set[i] = Mapping[current_set[i]]
#     lowest = min(current_set)
# print(lowest)

#####Part 1 without Dictionary

# for mapping_lines in test[1:]:
#     dest = []
#     source = []
#     for line in mapping_lines.split("\n"):
#         if line!="" and line[0].isnumeric():
#             d, s, x = [int(x) for x in line.split(' ')]
#             dest+=[i for i in range(d, d+x)]
#             source+=[i for i in range(s, s+x)]
#     for i in range(len(current_set)):
#         if current_set[i] in source:
#             current_set[i] = dest[source.index(current_set[i])]
#     lowest = min(current_set)
# print(lowest)

#####Part 1 with Math

# for mapping_lines in test[1:]:
#     d = []
#     s = []
#     x = []
#     new_set = current_set[:]
#     for line in mapping_lines.split("\n"):
#         if line!="" and line[0].isnumeric():
#             dest, source, ranges = [int(x) for x in line.split(' ')]
#             d.append(dest)
#             s.append(source)
#             x.append(ranges)
#         else:
#             continue
#     for j in range (len(d)):
#         for i in range(len(new_set)):
#             if current_set[i] >= s[j] and current_set[i]<s[j] + x[j]:
#                 new_set[i] = current_set[i] - s[j] + d[j]
#     current_set = new_set[:]
#     lowest = min(current_set)
# print(lowest)


#####Part 2 brute force
# current_set = []
# for i in range(0, len(seeds), 2):
#     current_set += [i for i in range(seeds[i], seeds[i] + seeds[i+1])]

# for mapping_lines in test[1:]:
#     d = []
#     s = []
#     x = []
#     new_set = current_set[:]
#     for line in mapping_lines.split("\n"):
#         if line!="" and line[0].isnumeric():
#             dest, source, ranges = [int(x) for x in line.split(' ')]
#             d.append(dest)
#             s.append(source)
#             x.append(ranges)
#         else:
#             continue
#     for j in range (len(d)):
#         for i in range(len(new_set)):
#             if current_set[i] >= s[j] and current_set[i]<s[j] + x[j]:
#                 new_set[i] = current_set[i] - s[j] + d[j]
#     current_set = new_set[:]
#     lowest = min(current_set)
# print(current_set)

# print(lowest)

#####Part 2 memory problems


seed_nums =[]
seed_range = []
for i in range(0, len(seeds), 2):
    seed_nums += [seeds[i]]
    seed_range += [seeds[i+1]]
seed_set = zip(seed_nums, seed_range)
seed_set = sorted(seed_set, key = lambda t: t[0])

for mapping_lines in test[1:]:
    seed_set = sorted(seed_set, key = lambda t: t[0])
    d = []
    s = []
    x = []
    for line in mapping_lines.split("\n"):
        if line!="" and line[0].isnumeric():
            dest, source, ranges = [int(x) for x in line.split(' ')]
            d.append(dest)
            s.append(source)
            x.append(ranges)
        else:
            continue
        
    zipped = zip(d,s,x)
    zipped = sorted(zipped, key = lambda t: t[1])
    seed_count = 0
    map_count = 0
    while True:
            if seed_set[seed_count][0] >= zipped[map_count][1]:
                if seed_set[seed_count][0] + seed_set[seed_count][1] <= zipped[map_count][1] + zipped[map_count][2]:
                    seed_set[seed_count] = (seed_set[seed_count][0] - zipped[map_count][1] + zipped[map_count][0], seed_set[seed_count][1])
                    seed_count += 1
                    if seed_count >= len(seed_set):
                        break
                else:
                    if (seed_set[seed_count][0]>zipped[map_count][1] + zipped[map_count][2]):
                        map_count += 1
                        if map_count >= len(zipped):
                            break
                        continue
                    seed_set.insert(seed_count + 1, (zipped[map_count][1] + zipped[map_count][2], seed_set[seed_count][1] - ((zipped[map_count][1] + zipped[map_count][2]) - seed_set[seed_count][0])))
                    seed_set[seed_count] = (seed_set[seed_count][0] - zipped[map_count][1] + zipped[map_count][0], zipped[map_count][1] + zipped[map_count][2] - seed_set[seed_count][0])
                    map_count += 1
                    seed_count += 1
                    if map_count >= len(zipped):
                        break
            else:
                if seed_set[seed_count][1] > zipped[map_count][1] - seed_set[seed_count][0]:
                    seed_set.insert(seed_count + 1, (zipped[map_count][1], seed_set[seed_count][1] - (zipped[map_count][1] - seed_set[seed_count][0])))
                    seed_set[seed_count] = (seed_set[seed_count][0], zipped[map_count][1] - seed_set[seed_count][0])
                seed_count += 1
                if seed_count >= len(seed_set):
                    break

        
lowest = min([x[0] for x in seed_set])
    
print(lowest)
