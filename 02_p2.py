f = open("C:/Users/Bearson/Documents/2020_aoc/02.txt", "r")
l = f.read().split("\n")

data = []
for line in l:
    data.append(line.replace(":", "").replace("-", " ").split(" "))

valid = 0
flag = 0

for rule in data:
    for i in range(len(rule[3])):
        if rule[3][i] == rule[2]:
            if int(rule[0]) - 1 == i or int(rule[1]) - 1 == i:
                flag = flag + 1
    if flag == 1:
        valid = valid + 1
    flag = 0

print(valid)