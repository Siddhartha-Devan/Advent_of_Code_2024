with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

# print(len(inp))
inp = inp.split("mul")
# print(inp)

print(len(inp))
def bracket_verifier(inst):
    is_open = False
    open_ind = None
    is_closed = False
    closed_ind = None
    if inst[0] == "(":
        open_ind=0
        is_open = True
    
    if is_open==False:
        return None
    
    for i in range(1,len(inst)):
        if is_open:
            if inst[i] == "(" and is_closed == False:
                return None
            elif inst[i] == ")" and is_closed == False:
                is_closed = True
                closed_ind = i
                return (open_ind, i)

tot_sum = 0 
n = 0     
for i in inp:
    n+=1
    # print(i, bracket_verifier(i))
    indices = bracket_verifier(i)
    if indices != None:
        a, b = indices
        target = i[a+1:b]
        target = target.split(",")
        print(i, target)
        if len(target) == 2:
            if target[0].isnumeric() and target[1].isnumeric():
                n1 = int(target[0])
                n2 = int(target[1])
                # print(n, target, n1, n2)
                mul = n1*n2
                tot_sum+=mul

print(tot_sum)
print(n)

