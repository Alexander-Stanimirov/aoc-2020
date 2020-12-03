f = open("C:/Users/Username/Documents/2020_aoc/03.txt", "r")
l = f.read().split("\n")
grid = []
for line in l:
    grid.append(line*200)

def slope_change(right_inc, down_inc):
    hor = ver = found = 0
    
    while True:
        hor += right_inc
        ver += down_inc
        if grid[ver][hor] == "#":
            found += 1
        #print(ver, ", ", hor)
        if ver + down_inc >= len(grid):
            break
            
    return found
    
slope = [[1,1],[3,1],[5,1],[7,1],[1,2]]
result = 1

for i in range(len(slope)):
    result *= slope_change(slope[i][0], slope[i][1])
print(result)
