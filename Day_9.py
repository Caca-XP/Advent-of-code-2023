test = open('input9.txt', 'r')
test = test.read().split('\n')

##### Part 1

# def find_dif(data):
#     diffs = []
#     for i in range (0, len(data)-1):
#         diffs.append(data[i+1] - data[i])
#     print(diffs)
#     if all(x == 0 for x in diffs):
#         return data[-1]
#     else:
#         return data[-1] + find_dif(diffs)
    
    
# sum = 0
# for line in test:
#     if line != '':
#         data = [int(x) for x in line.split(' ')]
#         predicted = find_dif(data)
#         print(data, predicted)
#         sum += predicted

# print(sum)

##### Part 2
def find_dif_backward(data):
    diffs = []
    for i in range (0, len(data)-1):
        diffs.append(data[i+1] - data[i])
    print(diffs)
    if all(x == 0 for x in diffs):
        return data[0]
    else:
        return data[0] - find_dif_backward(diffs)
    
    
sum = 0
for line in test:
    if line != '':
        data = [int(x) for x in line.split(' ')]
        predicted = find_dif_backward(data)
        print(data, predicted)
        sum += predicted

print(sum)