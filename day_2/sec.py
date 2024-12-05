with open ('sup_1.txt', 'r') as file:
    inp = file.read()
    file.close()
    # print(inp)

sup_1 = inp.split("\n")
# print(inp)
# print(inp[1].split(","))
# inp = [i.split(" ") for i in inp] 
# # print(inp)

# inp = [[int(i) for i in j] for j in inp]



with open ('sup_2.txt', 'r') as file:
    inp = file.read()
    # print(inp)

sup_2 = inp.split("\n")
# print(inp)

# inp = [i.split(" ") for i in inp] 
# # print(inp)

# sup_2 = [[int(i) for i in j] for j in inp]

for i in range(len(sup_2)):
    print(sup_1[i]==sup_2[i])