f = open("C:/Users/Username/Documents/2020_aoc/02.txt", "r")
l = f.read().split("\n")

data = []
for line in l:
    data.append(line.replace(":", "").replace("-", " ").split(" "))

count = valid = 0

for rule in data:
    for c in rule[3]:
        if c == rule[2]:
            count = count + 1
    if count >= int(rule[0]) and count <= int(rule[1]):
        valid = valid + 1
    count = 0

print(valid)
