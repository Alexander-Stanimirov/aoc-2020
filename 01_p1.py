f = open("C:/Users/Username/Documents/2020_aoc/01.txt", "r")
nums_s = f.read().split("\n")
ints_low = []
ints_high = []
for n in nums_s:
    if int(n) <= 2020/2:
        ints_low.append(int(n))
    else:
        ints_high.append(int(n))

for l in ints_low:
    for h in ints_high:
        if l + h == 2020:
            print(l*h)
