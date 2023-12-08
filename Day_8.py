test = open('input8.txt', 'r')
test = test.read().split('\n')

instructions = test[0]
print(instructions)
Graph = {}
LEFT = 0
RIGHT = 1


##### Part 1
# curr = 'AAA'
# dest = 'ZZZ'

# for line in test[1:]:
#     if line == '':
#         continue
#     line = line.replace('(', '').replace(')', '').split(' = ')
#     node = line.pop(0)
#     left, right = line[0].replace(' ', '').split(',')
#     if node not in Graph:
#         Graph[node] = [left, right]

# passes = 0
# while curr != dest:
#     for dir in instructions:
#         if dir == 'L':
#             curr = Graph[curr][LEFT]
#         elif dir == 'R':
#             curr = Graph[curr][RIGHT]
#         passes += 1
#         # print(curr)
#         if curr == dest:
#             break
        
# print(passes)


##### Part 2
curr = []
dest = []

for line in test[1:]:
    if line == '':
        continue
    line = line.replace('(', '').replace(')', '').split(' = ')
    node = line.pop(0)
    left, right = line[0].replace(' ', '').split(',')
    if node not in Graph:
        Graph[node] = [left, right]
    if node[-1] == 'A':
        curr.append(node)
    elif node[-1] == 'Z':
        dest.append(node)


passes = [0] * len(curr)
# while every element in curr is not in dest
while not all(elem in dest for elem in curr):
    for dir in instructions:
        if dir == 'L':
            for i in (j for j, x in enumerate(curr) if x not in dest):
                curr[i] = Graph[curr[i]][LEFT]
                passes[i] += 1
        elif dir == 'R':
            for i in (j for j, x in enumerate(curr) if x not in dest):
                curr[i] = Graph[curr[i]][RIGHT]
                passes[i] += 1
        print(curr)
        if all(elem in dest for elem in curr):
            break
        
result = 1
passes = sorted(passes, reverse=True)
print(passes)


def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

for i in range(len(passes)):
    factors = find_factors(passes[i])
    for f in factors:
        if result % f != 0:
            result *= f

print(result)




##### Part 2 brute force
 
# passes = 0
# # while every element in curr is not in dest
# while not all(elem in dest for elem in curr):
#     for dir in instructions:
#         if dir == 'L':
#             curr = [Graph[x][LEFT] for x in curr]
#         elif dir == 'R':
#             curr = [Graph[x][RIGHT] for x in curr]
#         print(curr)
#         passes += 1
#         if all(elem in dest for elem in curr):
#             break
        
# print(passes)
