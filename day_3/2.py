with open ('inp.txt', 'r') as file:
    inp = file.read()
    inp = inp.replace("\n", "")
    # print(inp)
    # hvu_mul(4,5)dj0923jdo()_vov_don'tmuldon't()_knjci_mul
# inp = "knjci_mul(5,6)jnscdon't()ncddon't()klnsm_do()_jihidon't()iiwd_don't()mul(2,2)odo()kj"
# print(len(inp))
    # if "\n" in inp:
    #     print("shit")
    # while "\n" in inp:
    #     inp = inp.replace("\n", "")

        
inp = inp.split("mul")
print(inp)

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
is_enabled = True
prev_mode = True
new_en = 0
for i in inp:
    # n+=1
    
    if len(i)==4:
        if i == "do()":
            print("Trued")
            prev_mode = is_enabled
            is_enabled = True
            new_en = 1
    elif len(i)==7:
        if i == "don't()":
            print("Falsed")
            prev_mode = is_enabled
            is_enabled = False
            new_en = 1
    elif len(i)>4 and len(i)<7:
        # print("yes...", i)
        for j in range(0, len(i)-3):
            if i[j:j+4] == 'do()':
                print("Trued", i[j:j+4])
                prev_mode = is_enabled
                is_enabled = True
                new_en = 1

    elif len(i)>7:
        should_i_do = 0
        should_i_dont = 0
        # print("olunga paaru: ", i)
        for j in range(0,len(i)-3):
            if i[j:j+4] == "do()":
                print("Trued", i[j:j+4], j, j+4)
                # prev_mode = is_enabled
                # is_enabled=True
                should_i_do = 1
                should_i_dont = 0
                new_en = 1
            else: print("",end = "")
            # if j+6<len(i):
                # print(i[j:j+7], j, j+7, len(i))
            if i[j:j+7] == "don't()":
                print("Falsed", i[j:j+7], j, j+7)
                # prev_mode = is_enabled
                # is_enabled = False
                should_i_dont =1
                should_i_do = 0
                new_en=1
        if should_i_do == 1:
            prev_mode = is_enabled
            is_enabled=True
        if should_i_dont == 1:
            prev_mode = is_enabled
            is_enabled = False
        print(i, is_enabled, prev_mode)


    indices = bracket_verifier(i)
    
    if indices != None:
        print(new_en)
        a, b = indices
        target = i[a+1:b]
        target = target.split(",")
        print(i, target)
        if len(target) == 2:
            if target[0].isnumeric() and target[1].isnumeric():
                if new_en == 0  and is_enabled==True:
                    n1 = int(target[0])
                    n2 = int(target[1])
                    print(n, target, n1, n2)
                    mul = n1*n2
                    tot_sum+=mul
                    n+=1

                elif new_en == 1 and prev_mode == True and is_enabled ==True:
                    n1 = int(target[0])
                    n2 = int(target[1])
                    print(n, target, n1, n2)
                    mul = n1*n2
                    tot_sum+=mul
                    n+=1
                    # print("skipped")

                elif new_en == 1 and prev_mode == False and is_enabled ==True:
                    # n1 = int(target[0])
                    # n2 = int(target[1])
                    # print(n, target, n1, n2)
                    # mul = n1*n2
                    # tot_sum+=mul
                    # n+=1
                    print("skipped")

                elif new_en == 1 and prev_mode ==True  and is_enabled==False:
                    n1 = int(target[0])
                    n2 = int(target[1])
                    print(n, target, n1, n2)
                    mul = n1*n2
                    tot_sum+=mul
                    n+=1
                elif new_en == 1 and prev_mode == False and is_enabled ==False:
                    # n1 = int(target[0])
                    # n2 = int(target[1])
                    # print(n, target, n1, n2)
                    # mul = n1*n2
                    # tot_sum+=mul
                    # n+=1
                    print("skipped")


    new_en = 0
print(tot_sum)
print(n)
# for i in inp:
#     print(i)












    # # print(i, bracket_verifier(i))
    # if "don't()" in i:
    #     print("dont:  ", i)
    #     is_enabled=False
    # if "do()" in i:
    #     print("do:  ",i)
    #     is_enabled = True