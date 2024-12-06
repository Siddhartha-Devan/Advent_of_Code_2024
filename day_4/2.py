with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)
mat = [list(i) for i in inp]

print(mat)
print(len(mat), len(mat[0]))

x_mas=0
for i in range(1, len(mat)-1):
    for j in range(1, len(mat)-1):
        if mat[i][j] == 'A':
            checker_1 = [mat[i-1][j-1], mat[i+1][j+1]]
            checker_2 = [mat[i+1][j-1], mat[i-1][j+1]]

            mc_1 = checker_1.count('M')
            mc_2 = checker_2.count('M')
            sc_1 = checker_1.count('S')
            sc_2 = checker_2.count('S')

            if mc_1==1 and mc_2 == 1 and sc_1 == 1 and sc_2 == 1:
                x_mas+=1
print(x_mas)

