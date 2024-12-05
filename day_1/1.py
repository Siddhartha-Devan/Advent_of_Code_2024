with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)


left = []
right = []
# print(inp)

inp = inp.split("\n")
print(inp)

for i in inp:
    items = i.split(" ")
    # print(items)
    left.append(int(items[0]))
    right.append(int(items[-1]))

left.sort()
right.sort()

# print(left)
# print(right)

diff_list = []
sum_ = 0
for i in range(len(left)):
    dist = abs(left[i] - right[i])
    sum_+= dist
    diff_list.append(dist)

print(sum_)