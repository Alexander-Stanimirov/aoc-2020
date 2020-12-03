f = open("C:/Users/Username/Documents/2020_aoc/01_bigboy.txt", "r")
nums_s = f.read().split("\n")
ints_low = []
ints_all = []
ints_high = []
for n in nums_s:
    ints_all.append(int(n))
    if int(n) <= 2020/2:
        ints_low.append(int(n))
    else:
        ints_high.append(int(n))

for a in ints_all:
    for l in ints_low:
        for h in ints_high:
            if l + h + a == 2020:
                print(l*h*a)

