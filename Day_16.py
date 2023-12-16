test = open('input16.txt', 'r')
test = test.read().split('\n')
test = [x for x in test if x != '']

mirror = {'/': {'U': 'R', 'D': 'L', 'R': 'U', 'L': 'D'}, '\\': {'U': 'L', 'D': 'R', 'R': 'D', 'L': 'U'}}
spliter = {'-': {'U': ['L', 'R'], 'D': ['L', 'R']}, '|': {'R': ['U', 'D'], 'L': ['U', 'D']}}
dir = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}

##### Part 1
# queue = []
# visited = []
# curr = [0, 0]
# curr_dir = 'R'
# if test[0][0] == '|':
#     curr_dir = 'D'
# elif test[0][0] == '\\':
#     curr_dir = 'D'
# elif test[0][0] == '/':
#     curr_dir = 'U'


# while True:
#     visited.append([curr, curr_dir])
#     next = [curr[0] + dir[curr_dir][0], curr[1] + dir[curr_dir][1]]
#     if next[0] < 0 or next[0] >= len(test) or next[1] < 0 or next[1] >= len(test[0]):
#         if len(queue) == 0:
#             break
#         curr, curr_dir = queue.pop()
#         continue

#     if test[next[0]][next[1]] in mirror.keys():
#         curr_dir = mirror[test[next[0]][next[1]]][curr_dir]
        
#     if test[next[0]][next[1]] in spliter.keys():
#         # print(test[next[0]][next[1]], curr_dir, spliter[test[next[0]][next[1]]][curr_dir])
#         if curr_dir in spliter[test[next[0]][next[1]]].keys():
#             queue.append([next, spliter[test[next[0]][next[1]]][curr_dir][1]])
#             curr_dir = spliter[test[next[0]][next[1]]][curr_dir][0]
#     curr = next
    
#     if [curr, curr_dir] in visited:
#         if len(queue) == 0:
#             break
#         curr, curr_dir = queue.pop()
        
# # find the number of unique coordinates in visited
# unique = []
# for i in visited:
#     if i[0] not in unique:
#         unique.append(i[0])

# print(len(unique))
    
    
    
    
##### Part 2
edge_tiles = []
edge_queue = []
for i in range(0, len(test)):
    if [i, 0] not in edge_tiles and [i, len(test[0])-1] not in edge_tiles:
        edge_tiles.append([i, 0])
        edge_tiles.append([i, len(test[0])-1])
for j in range(0, len(test[0])):
    if [0, j] not in edge_tiles and [len(test)-1, j] not in edge_tiles:
        edge_tiles.append([0, j])
        edge_tiles.append([len(test)-1, j])
        
print(len(edge_tiles))
for tile in edge_tiles:
    # if corner try both directions
    # else go in direction away from edge
    if tile[0] == 0:
        edge_queue.append([tile, 'D'])
    if tile[0] == len(test)-1:
        edge_queue.append([tile, 'U'])
    if tile[1] == 0:
        edge_queue.append([tile, 'R'])
    if tile[1] == len(test[0])-1:
        edge_queue.append([tile, 'L'])

longest = 0
for curr, curr_dir in edge_queue:
    print(curr, curr_dir)
    queue = []
    visited = []
    if test[curr[0]][curr[1]] == '|':
        # print('|')
        curr_dir = 'D'
        queue.append([curr, 'U'])
    elif test[curr[0]][curr[1]] == '\\':
        # print('\\')
        curr_dir = mirror['\\'][curr_dir]
    elif test[curr[0]][curr[1]] == '/':
        # print('/')
        curr_dir = mirror['/'][curr_dir]
    elif test[curr[0]][curr[1]] == '-':
        # print('-')
        curr_dir = 'R'
        queue.append([curr, 'L'])

    while True:
        visited.append([curr, curr_dir])
        next = [curr[0] + dir[curr_dir][0], curr[1] + dir[curr_dir][1]]
        if next[0] < 0 or next[0] >= len(test) or next[1] < 0 or next[1] >= len(test[0]):
            if len(queue) == 0:
                break
            curr, curr_dir = queue.pop()
            continue

        if test[next[0]][next[1]] in mirror.keys():
            curr_dir = mirror[test[next[0]][next[1]]][curr_dir]
            
        if test[next[0]][next[1]] in spliter.keys():
            # print(test[next[0]][next[1]], curr_dir, spliter[test[next[0]][next[1]]][curr_dir])
            if curr_dir in spliter[test[next[0]][next[1]]].keys():
                queue.append([next, spliter[test[next[0]][next[1]]][curr_dir][1]])
                curr_dir = spliter[test[next[0]][next[1]]][curr_dir][0]
        curr = next
        
        if [curr, curr_dir] in visited:
            if len(queue) == 0:
                break
            curr, curr_dir = queue.pop()
            
    # find the number of unique coordinates in visited
    unique = []
    for i in visited:
        if i[0] not in unique:
            unique.append(i[0])
    if len(unique) > longest:
        longest = len(unique)
        print(longest)

print('*'*30)
print(longest)