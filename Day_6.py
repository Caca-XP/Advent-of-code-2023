test = open('input6.txt', 'r')
line = test.read().split('\n')


##### Part 1
# time = [int(i) for i in list(filter(None, line[0].split(' ')[1:]))]
# record = [int(i) for i in list(filter(None, line[1].split(' ')[1:]))]

# print(time)
# print(record)

# prod = 1

# for race in range(len(time)):
#     num_wins = 0
#     for milisec in range(time[race]):
#         speed = milisec
#         dist = speed*(time[race] - milisec)
#         if dist > record[race]:
#             num_wins+=1
#     prod*=num_wins

# print(prod)


#####Part 1 with smarts
time = [int(i) for i in list(filter(None, line[0].split(' ')[1:]))]
record = [int(i) for i in list(filter(None, line[1].split(' ')[1:]))]

print(time)
print(record)

prod = 1

for race in range(len(time)):
    num_wins = 0
    min_win = -1
    max_win = -1

    milisec = 0
    for milisec in range(time[race]):
        speed = milisec
        dist = speed*(time[race] - milisec)
        if dist > record[race]:
            if min_win == -1:
                min_win = milisec
                break
    max_win = time[race]-min_win
    num_wins = max_win - min_win + 1
    prod*=num_wins

print(prod)
print("*"* 30)

##### Part 2 brute force
# time = int("".join([i for i in list(filter(None, line[0].split(' ')[1:]))]))
# record = int("".join([i for i in list(filter(None, line[1].split(' ')[1:]))]))


# print(time)
# print(record)

# num_wins = 0

# for milisec in range(time):
#     speed = milisec
#     dist = speed*(time - milisec)
#     if dist > record:
#         num_wins+=1

# print(num_wins)

##### Part 2 with smarts
time = int("".join([i for i in list(filter(None, line[0].split(' ')[1:]))]))
record = int("".join([i for i in list(filter(None, line[1].split(' ')[1:]))]))


print(time)
print(record)

num_wins = 0
min_win = -1
max_win = -1

for milisec in range(time):
    speed = milisec
    dist = speed*(time - milisec)
    if dist > record:
        if min_win == -1:
            min_win = milisec
            break
max_win = time-min_win

num_wins = max_win - min_win + 1
print(num_wins)