from copy import deepcopy as dc

with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)
mat = [list(i) for i in inp]

# print(mat)
print(len(mat), len(mat[0]))

# map_copy = map.copy()
# curr_pos = [0,0]
# for i in range(len(map)):
#     for j in range(len(map[0])):
#         if map[i][j] == "^":
#             curr_pos = [i,j]

# print(curr_pos)
# map_copy[curr_pos[0]][curr_pos[1]] = 'X'
# # print(map_copy)
 
# row = curr_pos[0]
# col = curr_pos[1]
# movement = "up"

# while (row <len(map)-1 and col <len(map)-1) and (row>0 and col>0):
#     if movement == 'up':
#         row-=1
#         if map[row][col] == "#":
#             row+=1
#             movement = 'right'
#         else:
#             map_copy[row][col] = "X"
#             curr_pos = [row, col]

#     if movement == "right":
#         col+=1
#         if map[row][col] == "#":
#             col-=1
#             movement = 'down'
#         else:
#             map_copy[row][col] = "X"
#             curr_pos = [row, col]

#     if movement == 'down':
#         row+=1
#         if map[row][col] == "#":
#             row-=1
#             movement = 'left'
#         else:
#             map_copy[row][col] = "X"
#             curr_pos = [row, col]
    
#     if movement == 'left':
#         col-=1
#         if map[row][col] == "#":
#             col+=1
#             movement = 'up'
#         else:
#             map_copy[row][col] = "X"
#             curr_pos = [row, col]
    
# print(curr_pos)

# tot_visited = 0
# for i in map_copy:
#     tot_visited+=i.count('X')

# print(tot_visited)

# r = 0
# c = 0
# map_c = map.copy()
# map_c[r][c] = '#'
# loopers = []

def is_loop(map):
    map_copy = map.copy()
    start_pos = [6,4]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                start_pos = [i,j]

    print(start_pos)
    start_movement = 'up'
    curr_pos = start_pos.copy()
    # curr_pos = [6, 4]
    # map_copy[curr_pos[0]][curr_pos[1]] = 'X'
    # print(map_copy)
    
    row = curr_pos[0]
    col = curr_pos[1]
    movement = "up"

    n_steps = 0
    while (row <len(map)-1 and col <len(map)-1) and (row>0 and col>0):
        if n_steps%30000 == 0:
            start_pos = curr_pos
            start_movement = movement
        if n_steps%30001 == 0:
            start_pos = curr_pos
            start_movement = movement
        if n_steps>500000:
            if start_pos == curr_pos:
                print(start_pos, movement, start_movement)
        if movement == 'up':
            row-=1
            n_steps+=1
            if map[row][col] == "#":
                row+=1
                movement = 'right'
            else:
                # map_copy[row][col] = "X"
                curr_pos = [row, col]
            if curr_pos == start_pos and start_movement == movement:
                print("loop uh", curr_pos, movement, n_steps)
                return True

        if movement == "right":
            col+=1
            n_steps+=1
            if map[row][col] == "#":
                col-=1
                movement = 'down'
            else:
                # map_copy[row][col] = "X"
                curr_pos = [row, col]
            if curr_pos == start_pos and start_movement == movement:
                print("loop uh", curr_pos, movement, n_steps)
                return True
                
        if movement == 'down':
            row+=1
            n_steps+=1
            if map[row][col] == "#":
                row-=1
                movement = 'left'
            else:
                # map_copy[row][col] = "X"
                curr_pos = [row, col]
            if curr_pos == start_pos and start_movement == movement:
                print("loop uh", curr_pos, movement, n_steps)
                return True
        
        if movement == 'left':
            col-=1
            n_steps+=1
            if map[row][col] == "#":
                col+=1
                movement = 'up'
            else:
                # map_copy[row][col] = "X"
                curr_pos = [row, col]
            if curr_pos == start_pos and start_movement == movement:
                print("loop uh", curr_pos, movement, n_steps, "fu")
                return True
        
        # if curr_pos == start_pos and start_movement == movement:
        #     print("loop uh", curr_pos)
        #     return True
    # print(curr_pos)
    print(curr_pos, movement, n_steps)
    # print(map[5][4])
    return False



map_c = dc(mat)
map_c[6][3] = "#"
print(is_loop(map=map_c))
print(mat[6][3])

loopers = []
for r in range(len(mat)):
    for c in range(len(mat)):
        map_c = dc(mat)
        if map_c[r][c] != '^' and map_c[r][c] != "#":
            map_c[r][c] = '#'
            print("new_obs:",r,c)
            if is_loop(map_c) == True:
                loopers.append([r,c])
                print(loopers)

            map_c = None

print(loopers)
print("n_loops =", len(loopers))