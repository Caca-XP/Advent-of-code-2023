test = open("input4.txt", "r")
test = test.read().split("\n")


# #####Part 1
# sum = 0
# for line in test:
#     if line == "":
#         continue
#     CardNum = line[:line.find(":")]
#     print(CardNum, end=" ")
#     point = 0
#     sets = line[line.find(":")+2:].split(" | ")
#     winning_set = sets[0]
#     held_set = sets[1]
#     winning_numbs = []
#     num = ""
#     for i in range(len(winning_set) + 1):
#         if i == len(winning_set) or winning_set[i] == " ":
#             if num != "":
#                 winning_numbs.append(int(num))
#             num = ""
#             continue
#         else:
#             num += winning_set[i]
#     for i in range(len(held_set) + 1):
#         if i == len(held_set) or held_set[i] == " ":
#             if num != "":
#                 if int(num) in winning_numbs:
#                     if point==0:
#                         point+=1
#                     else:
#                         point*=2
#             num = ""
#             continue
#         else:
#             num += held_set[i]
#     sum += point
#     print(point)
    
# print(sum)


#####Part 2
sum = 0
card_dict = {x:1 for x in range(1, len(test))}
for line in test:
    if line == "":
        continue
    CardNum = int(line[:line.find(":")].replace(" ", "").replace("Card", ""))
    wins = 0
    sets = line[line.find(":")+2:].split(" | ")
    winning_set = sets[0]
    held_set = sets[1]
    winning_numbs = []
    num = ""
    for i in range(len(winning_set) + 1):
        if i == len(winning_set) or winning_set[i] == " ":
            if num != "":
                winning_numbs.append(int(num))
            num = ""
            continue
        else:
            num += winning_set[i]
    for i in range(len(held_set) + 1):
        if i == len(held_set) or held_set[i] == " ":
            if num != "":
                if int(num) in winning_numbs:
                    wins += 1
            num = ""
            continue
        else:
            num += held_set[i]
    for card in range(1, wins+1):
        card_dict[card + CardNum] += card_dict[CardNum]
    
print()
print(card_dict)

for value in card_dict.values():
    sum += value
print(sum)