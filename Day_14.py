test = open('input14.txt', 'r')
test = test.read().split('\n')
# remove any empty test[l]s
test = [list(line) for line in test if line != '']

##### Part 1
# sum = 0
# length = len(test)
# for l in range(len(test)):
#     for i in range(0, len(test[l])):
#         if test[l][i] == 'O':
#             start = l
#             while start > 0 and test[start-1][i] not in 'O#':
#                 test[start][i] = '.'
#                 test[start-1][i] = 'O'
#                 start -= 1
#             sum+=length-start
# # for line in test:
# #     print(line)

# print(sum)



##### Part 2
prev_cycle = [row[:] for row in test]
prev_cycles = [prev_cycle]
before = 0
loop = 0
length = len(test)
sum = 0
for _ in range(1000000000):
    # North
    for l in range(len(test)):
        for i in range(0, len(test[l])):
            if test[l][i] == 'O':
                start = l
                while start > 0 and test[start-1][i] not in 'O#':
                    test[start][i] = '.'
                    test[start-1][i] = 'O'
                    start -= 1

    # West
    for l in range(len(test)):
        for i in range(0, len(test[l])):
            if test[l][i] == 'O':
                start = i
                while start > 0 and test[l][start-1] not in 'O#':
                    test[l][start] = '.'
                    test[l][start-1] = 'O'
                    start -= 1

    # South
    for l in range(len(test)-1, -1, -1):
        for i in range(len(test[l])-1, -1, -1):
            if test[l][i] == 'O':
                start = l
                while start < len(test)-1 and test[start+1][i] not in 'O#':
                    test[start][i] = '.'
                    test[start+1][i] = 'O'
                    start += 1

    # East
    for l in range(len(test)-1, -1, -1):
        for i in range(len(test[l])-1, -1, -1):
            if test[l][i] == 'O':
                start = i
                while start < len(test[l])-1 and test[l][start+1] not in 'O#':
                    test[l][start] = '.'
                    test[l][start+1] = 'O'
                    start += 1

    if test in prev_cycles:
        for prev in prev_cycles:
            if prev == test:
                before += prev_cycles.index(prev)
                print(before)
                break
        loop = _+1 - before
        print(_, loop)
        break
    prev_cycle = [row[:] for row in test]
    prev_cycles.append(prev_cycle)

x = 1000000000
y = (x-before)//loop
print(y)
index = x - y*loop
print(index)
test = prev_cycles[index]

sum = 0
for l in range(len(test)):
    for i in range(0, len(test[l])):
        if test[l][i] == 'O':
            sum+=length-l


print(sum)
