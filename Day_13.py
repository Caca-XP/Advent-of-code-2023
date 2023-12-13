test = open('input13.txt', 'r')
test = test.read().split('\n\n')
test[-1] = test[-1][:-1]


##### Part 1
# col = 0
# row = 0
# horizontal = False
# for line in test:
#     if line != '':
#         i = 1
#         line = line.split('\n')
#         while i < len(line):
#             if line[i-1] == line[i]:
#                 up = i-1
#                 down = i
#                 while up >= 0 and down < len(line) and line[up] == line[down]:
#                     up -= 1
#                     down += 1
#                 if up == -1 or down == len(line):
#                     row += i
#                     horizontal = True
#                     break
#             i += 1
#         if horizontal:
#             horizontal = False
#             continue
#         # transpose line
#         line = list(zip(*line))
#         i = 1
#         while i < len(line):
#             if line[i-1] == line[i]:
#                 up = i-1
#                 down = i
#                 while up >= 0 and down < len(line) and line[up] == line[down]:
#                     up -= 1
#                     down += 1
#                 if up == -1 or down == len(line):
#                     col += i
#                     break
#             i += 1
        


# print(row*100 + col)




##### Part 2
col = 0
row = 0
horizontal = False
for t in range(len(test)):
    if test[t] != '':
        i = 1
        line = test[t].split('\n')
        while i < len(line):
            line = test[t].split('\n')
            diff = 0
            wrong = 0
            for j in range(0, len(line[i-1])):
                if line[i-1][j] != line[i][j]:
                    wrong += 1
            if wrong == 1:
                line[i-1] = line[i]
                diff += 1
            if line[i-1] == line[i]:
                up = i-1
                down = i
                while up >= 0 and down < len(line) and (line[up] == line[down] or diff < 1):
                    if line[up] != line[down]:
                        # if only one char is different
                        wrong = 0
                        for j in range(0, len(line[up])):
                            if line[up][j] != line[down][j]:
                                wrong += 1
                        if wrong != 1:
                            break
                        diff += 1
                    up -= 1
                    down += 1
                if (up == -1 or down == len(line)) and diff == 1:
                    row += i
                    horizontal = True
                    break
            i += 1
            
        if horizontal:
            horizontal = False
            continue

        i = 1
        line = test[t].split('\n')
        line = list(zip(*line))
        while i < len(line):
            line = test[t].split('\n')
            line = list(zip(*line))
            diff = 0
            wrong = 0
            for j in range(0, len(line[i-1])):
                if line[i-1][j] != line[i][j]:
                    wrong += 1
            if wrong == 1:
                line[i-1] = line[i]
                diff += 1
            if line[i-1] == line[i]:
                up = i-1
                down = i
                while up >= 0 and down < len(line) and (line[up] == line[down] or diff < 1):
                    if line[up] != line[down]:
                        # if only one char is different
                        wrong = 0
                        for j in range(0, len(line[up])):
                            if line[up][j] != line[down][j]:
                                wrong += 1
                        if wrong != 1:
                            break
                        diff += 1
                    up -= 1
                    down += 1
                if (up == -1 or down == len(line)) and diff == 1:
                    col += i
                    break
            i += 1            
        


print(row*100 + col)