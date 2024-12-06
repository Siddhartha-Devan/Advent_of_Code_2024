with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)
mat = [list(i) for i in inp]

# print(mat)
print(len(mat), len(mat[0]))

target = 'XMAS'
n_xmas_rows = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j:j+4] == list(target):
            n_xmas_rows+=1
        if mat[i][j:j+4] == list(target)[::-1]:
            n_xmas_rows+=1

print(n_xmas_rows)

n_xmas_cols = 0
for i in range(len(mat)):
    for j in range(len(mat)-3):
        # print(i,j)
        parsed = mat[j][i]+mat[j+1][i] +mat[j+2][i]+mat[j+3][i]
        if parsed == target:
            # print(i,j)
            n_xmas_cols+=1
        if parsed == target[::-1]:
            # print(i,j)
            n_xmas_cols+=1
print(n_xmas_cols)

n_xmas_diags_lr = 0

i = 0
j = len(mat)-4
i_init = 0
j_init = len(mat)-4
n_digs = (len(mat)*2) - 6
r = 4

while r<=len(mat):
    for d in range(r-3):
        parsed = mat[i][j]+mat[i+1][j+1]+mat[i+2][j+2]+mat[i+3][j+3]
        # print(parsed, i, j)

        if parsed == target:
            n_xmas_diags_lr += 1
        if parsed == target[::-1]:
            n_xmas_diags_lr+=1
        i+=1
        j+=1

    j_init-=1
    i = i_init
    j = j_init

    
    r+=1

j = 0
i = len(mat)-4
j_init = 0
i_init = len(mat)-4

r = 4
while r<=len(mat)-1:
    for d in range(r-3):
        parsed = mat[i][j] + mat[i+1][j+1] + mat[i+2][j+2] + mat[i+3][j+3]
        # print(parsed, i, j)
        if parsed == target:
            n_xmas_diags_lr += 1
        if parsed == target[::-1]:
            n_xmas_diags_lr+=1

        i+=1
        j+=1
    i_init-=1
    i = i_init
    j = j_init
    
    r+=1
    

print("n_xmas_diags_lr: ", n_xmas_diags_lr)


n_xmas_diags_rl = 0

i = 3
j = 0
i_init = 3
j_init = 0

r = 4
while r<=len(mat):
    for d in range(r-3):
        parsed = mat[i][j] + mat[i-1][j+1] + mat[i-2][j+2] + mat[i-3][j+3] 
        # print(parsed, i , j)

        if parsed == target:
            n_xmas_diags_rl += 1
        if parsed == target[::-1]:
            n_xmas_diags_rl += 1

        i-=1
        j+=1

    i_init+=1
    i = i_init
    j = j_init
    r+=1






i = len(mat)-1
j = len(mat)-4
i_init = len(mat)-1
j_init = len(mat)-4

r = 4
while r<=len(mat)-1:
    for d in range(r-3):
        parsed = mat[i][j] + mat[i-1][j+1] + mat[i-2][j+2] + mat[i-3][j+3]
        # print(parsed, i, j)
        if parsed == target:
            n_xmas_diags_rl+=1
        if parsed == target[::-1]:
            n_xmas_diags_rl+=1 
        i-=1
        j+=1

    j_init-=1
    i = i_init
    j = j_init

    r+=1


print("n_xmas_diags_rl:", n_xmas_diags_rl)


tot = n_xmas_rows + n_xmas_cols + n_xmas_diags_lr + n_xmas_diags_rl
print("total: ",tot)
