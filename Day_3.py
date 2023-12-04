test = open("input3.txt", "r")
test = test.read().split("\n")

EAST = [0, 1]
SOUTH = [1, 0]
WEST = [0, -1]
NORTH = [-1, 0]
NORTH_EAST = [-1, 1]
SOUTH_EAST = [1, 1]
SOUTH_WEST = [1, -1]
NORTH_WEST = [-1, -1]

directions = [EAST, SOUTH, WEST, NORTH, NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST]
#####Part 1
# sum = 0

# for i in range(len(test)):
#     if test[i] == "":
#         continue
#     num = ""
#     add = False
#     for j in range(len(test[i])):
#         if(test[i][j] in "0123456789"):
#             num += test[i][j]
#             for dir in directions:
#                 if i+dir[0] >= 0 and i+dir[0] < len(test)-1 and j+dir[1] >= 0 and j+dir[1] < len(test[i]):
#                     if test[i+dir[0]][j+dir[1]] not in "0123456789.":
#                         add = True

#             # if at the end of line and add is True, add the number
#             if j == len(test[i])-1 and add:
#                 sum += int(num)
#                 if num != "":
#                     print(num, end=" ")
#         else:
#             if add:
#                 sum += int(num)
#                 if num != "":
#                     print(num, end=" ")
#             else:
#                 if num != "":
#                     print(num, end=" ")
#             num = ""
#             add = False
            
# print(sum)


#####Part 2        
sum = 0

for i in range(len(test)):
    if test[i] == "":
        continue
    num = []
    add = False
    for j in range(len(test[i])):
        if test[i][j] == "*":
            temp = ""
            for dir in directions:
                x = i + dir[0]
                y = j + dir[1]
                if x >= 0 and x < len(test)-1 and y >= 0 and y < len(test[i]):
                    if test[x][y] in "0123456789":
                        # traverse east and west until its no longer a number
                        # if it is a number, add it to num
                        temp = test[x][y]
                        while y+EAST[1] < len(test[i]) and test[x+EAST[0]][y+EAST[1]] in "0123456789":
                            temp += test[x+EAST[0]][y+EAST[1]]
                            x = x + EAST[0]
                            y = y + EAST[1]
                        x = i + dir[0]
                        y = j + dir[1]
                        while y+WEST[1] >= 0 and test[x+WEST[0]][y+WEST[1]] in "0123456789":
                            temp = test[x+WEST[0]][y+WEST[1]] + temp
                            x = x + WEST[0]
                            y = y + WEST[1]
                        if temp != "" and int(temp) not in num:
                            num.append(int(temp))
                            temp = ""
                            print(num)
            if len(num) == 2:
                ratio = num[0] * num[1]
                sum += ratio
            num = []

print(sum)