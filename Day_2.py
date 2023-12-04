test = open("input2.txt", "r")
test = test.read().split("\n")

##### Part 1

# skip = False
# cubes_dict = {"red": 12, "green": 13, "blue": 14}
# sum = 0

# for line in test:
#     GameID = line[:line.find(":")].replace("Game ", "")
#     if GameID == "":
#         continue
#     sets = line[line.find(":")+1:].replace(" ", "").split(";")
#     # print(sets)
#     for set in sets:
#         if set == "":
#             continue
#         set = set.split(",")
#         # print(set)
#         for cube in set:
#             for key, value in cubes_dict.items():
#                 if key in cube:
#                     num = int(cube.replace(key, ""))
#                     if num > value:
#                         # print("Game " + GameID + " is invalid")
#                         skip = True
#                         break
#             if skip:
#                 break
#         if skip:
#             break
#     if skip:
#         skip = False
#         continue
#     # print("Game " + GameID + " is valid")
#     sum += int(GameID)
    
# print(sum)



# Part 2
sum = 0

min_cubes_dict = {"red": 0, "green": 0, "blue": 0}

for line in test:
    GameID = line[:line.find(":")].replace("Game ", "")
    if GameID == "":
        continue
    sets = line[line.find(":")+1:].replace(" ", "").split(";")
    # print(sets)
    for set in sets:
        if set == "":
            continue
        set = set.split(",")
        # print(set)
        for cube in set:
            for key, value in min_cubes_dict.items():
                if key in cube:
                    num = int(cube.replace(key, ""))
                    if num > value:
                        min_cubes_dict[key] = num


    # print("Game " + GameID + " is valid")
    power = 1
    for value in min_cubes_dict.values():
        power *= value
    min_cubes_dict = {"red": 0, "green": 0, "blue": 0}
    sum += power
    
print(sum)
       