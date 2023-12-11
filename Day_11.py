test = open('input11.txt', 'r')
test = test.read().split('\n')

##### Part 1 (expansion_rate = 1)
# galaxies = []
# expanded = {'rows': [], 'cols': []}
# for i in range(0, len(test)):
#     if test[i] != '':
#         if '#' in test[i]:
#             for j in range(0, len(test[i])):
#                 if test[i][j] == '#':
#                     galaxies.append((i, j))
#         else:
#             expanded['rows'].append(i)

# expanded['cols'] = [i for i in range(0, len(test[0])) if i not in [x for _, x in galaxies]]
# print(expanded)
# map = ""
# for i in range(0, len(test)):
#     if i in expanded['rows']:
#         map += test[i] +'.'*len(expanded['cols'])+ '\n'+ '.'*(len(test[i])+ len(expanded['cols'])) + '\n'
#     else:
#         for j in range(0, len(test[i])):
#             if j in expanded['cols']:
#                 map += test[i][j] + '.'
#             else:
#                 map += test[i][j]
#         map += '\n'
# map = map.split('\n')
# # for i in range(0, len(map)):
# #     print(map[i])

# galaxies = []
# # update the galaxies coordinates
# for i in range(len(map)):
#     if map[i] != '':
#         if '#' in map[i]:
#             for j in range(0, len(map[i])):
#                 if map[i][j] == '#':
#                     galaxies.append((i, j))
        
# print(galaxies)

# sum = 0
# for i in range(0, len(galaxies)):
#     for j in range(i+1, len(galaxies)):
#         sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
# print(sum)


# ##### Part 2
galaxies = []
expanded = {'rows': [], 'cols': []}
expansion_rate = 1000000-1
for i in range(0, len(test)):
    if test[i] != '':
        if '#' in test[i]:
            for j in range(0, len(test[i])):
                if test[i][j] == '#':
                    galaxies.append((i, j))
        else:
            expanded['rows'].append(i)

expanded['cols'] = [i for i in range(0, len(test[0])) if i not in [x for _, x in galaxies]]
print(galaxies)
print(expanded)

new_galaxies = galaxies.copy()
for i in range(0, len(test)):
    if i in expanded['rows']:
        for g in range(0, len(galaxies)):
            if galaxies[g][0] >= i:
                new_galaxies[g] = (new_galaxies[g][0]+expansion_rate, new_galaxies[g][1])

for j in range(0, len(test[0])):
    if j in expanded['cols']:
        for g in range(0, len(galaxies)):
            if galaxies[g][1] >= j:
                new_galaxies[g] = (new_galaxies[g][0], new_galaxies[g][1]+expansion_rate)
        
print(new_galaxies)

sum = 0
for i in range(0, len(new_galaxies)):
    for j in range(i+1, len(new_galaxies)):
        sum += abs(new_galaxies[i][0] - new_galaxies[j][0]) + abs(new_galaxies[i][1] - new_galaxies[j][1])
print(sum)