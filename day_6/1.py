with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)
map = [list(i) for i in inp]

# print(mat)
print(len(map), len(map[0]))

map_copy = map.copy()
curr_pos = [0,0]
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "^":
            curr_pos = [i,j]

print(curr_pos)
map_copy[curr_pos[0]][curr_pos[1]] = 'X'
# print(map_copy)
 
row = curr_pos[0]
col = curr_pos[1]
movement = "up"

while (row <len(map)-1 and col <len(map)-1) and (row>0 and col>0):
    if movement == 'up':
        row-=1
        if map[row][col] == "#":
            row+=1
            movement = 'right'
        else:
            map_copy[row][col] = "X"
            curr_pos = [row, col]

    if movement == "right":
        col+=1
        if map[row][col] == "#":
            col-=1
            movement = 'down'
        else:
            map_copy[row][col] = "X"
            curr_pos = [row, col]

    if movement == 'down':
        row+=1
        if map[row][col] == "#":
            row-=1
            movement = 'left'
        else:
            map_copy[row][col] = "X"
            curr_pos = [row, col]
    
    if movement == 'left':
        col-=1
        if map[row][col] == "#":
            col+=1
            movement = 'up'
        else:
            map_copy[row][col] = "X"
            curr_pos = [row, col]
    
print(curr_pos)

tot_visited = 0
for i in map_copy:
    tot_visited+=i.count('X')

print(tot_visited)