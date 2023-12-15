test = open('input15.txt', 'r')
test = test.read().split('\n')

def HASH(s):
    curr = 0
    for c in s:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

##### Part 1


# sum = 0
# for line in test:
#     if line != '':
#         line = line.split(',')
#         for l in line:
#             sum += HASH(l)

# print(sum)

##### Part 2
HASHMAP = {}
for i in range(256):
    HASHMAP[i] = []

for line in test:
    if line != '':
        line = line.split(',')
        for l in line:
            if '-' in l:
                l = l.split('-')
                num = HASH(l[0])
                if HASHMAP[num] != []:
                    for lense in HASHMAP[num]:
                        if lense.split(' ')[0] == l[0]:
                            HASHMAP[num].remove(lense)
                            break
            if '=' in l:
                l = l.split('=')
                num = HASH(l[0])
                changed = False
                if HASHMAP[num] != []:
                    for lensenum in range(len(HASHMAP[num])):
                        if l[0] == HASHMAP[num][lensenum].split(' ')[0]:
                            HASHMAP[num][lensenum] = l[0] + ' ' + l[1]
                            changed = True
                            break
                if not changed:
                    HASHMAP[num].append(l[0] + ' ' + l[1])
                    

for i in range(256):
    if HASHMAP[i] != []:
        print(i, HASHMAP[i])


focusing_power = 0
for i in range(256):
    if HASHMAP[i] != []:
        for j in range(len(HASHMAP[i])):
            focal = int(HASHMAP[i][j].split(' ')[1])
            print((i+1) * (j+1) * focal)
            focusing_power += (i+1) * (j+1) * focal
                

print(focusing_power)
