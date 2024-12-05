with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)


left = []
right = []
# print(inp)

inp = inp.split("\n")
# print(inp)

for i in inp:
    items = i.split(" ")
    # print(items)
    left.append(int(items[0]))
    right.append(int(items[-1]))

left.sort()
right.sort()
left_set = set(left)
# print(left_set)
freq_dic = {}
for i in left_set:
    freq_dic[i] = -1
# print(freq_dic)


sim_score = 0

for i in left:
    if freq_dic[i] == -1:
        freq_i = right.count(i)
        freq_dic[i] = freq_i
        sim_score+=(freq_i*i)
    else:
        sim_score+=(freq_dic[i]*i)
# print(freq_dic)
print(sim_score)

