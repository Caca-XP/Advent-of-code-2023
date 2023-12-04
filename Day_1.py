input = open("input.txt", "r")
input = input.read().split("\n")

dict = {}
for i, englishNums in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
    dict[englishNums] = i

num = []
for line in input:
    number = ""
    for letter in range(0,len(line)):
        if line[letter] in "1234567890":
            number += line[letter]
        for key, value in dict.items():
            if key in line[letter:letter+len(key)]:
                number += str(value)
        
    if number != "":
        actual = number[0] + number[-1]
        num.append(int(actual))

sum = 0
for n in num:
    sum += n
    
print(sum)
print(num)