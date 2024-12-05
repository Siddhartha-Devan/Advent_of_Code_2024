with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)

inp = [i.split(" ") for i in inp] 
# print(inp)

inp = [[int(i) for i in j] for j in inp]
# print(inp)

def is_safe(report):
    is_incr = None
    for i in range(len(report)-1):
        a = report[i]
        b = report[i+1]
        if a>b:
            if a>b and is_incr==None:
                is_incr=False
            elif a>b and is_incr==False:
                is_incr = False
            elif a>b and is_incr==True:
                # print(report)
                # print(report)
                print("unakku ennada prachana", report,a,b, report[:i]+report[i:])
                # print('unsafe_lvl_1')
                if i+2<len(report):
                    if is_safe_inner(report[:i]+ report[i+1:]) or is_safe_inner(report[:i+1]+report[i+2:]) or is_safe_inner(report[:i-1]+report[i:]):
                        return 1
                    else:
                        # print("unsafe_2")
                        return 0
                else:
                    if is_safe_inner(report[:i]+report[i+1:]) or is_safe_inner(report[:i+1]):
                        return 1
                    else: 
                        # print("unsafe_2")
                        return 0
            else:
                # print("ada pongada...", report)
                return 0

        elif a<b:
            if a<b and is_incr == None:
                is_incr = True
            elif a<b and is_incr == True:
                is_incr = True
            elif a<b and is_incr==False:
                # print('unsafe_lvl_1')
                # print("neeya", report)
                if i+2<len(report):
                    # print("why", i)
                    print(report[:i] + report[i+1:], report[:i-1]+report[i:])
                    if is_safe_inner(report[:i] + report[i+1:]) or is_safe_inner(report[:i+1] +report[i+2:]) or is_safe_inner(report[:i-1]+report[i:]):
                        return 1
                    else:
                        # print("unsafe_2")
                        return 0
                else:
                    if is_safe_inner(report[:i]+report[i+1:]) or is_safe_inner(report[:i+1]):
                        return 1
                    else: 
                        # print("unsafe_2")
                        return 0

        
        
        diff = abs(a-b)
        if diff <1 or diff>3:
            # print('unsafe_lvl_1')
            if i+2<len(report):
                if is_safe_inner(report[:i]+ report[i+1:]) or is_safe_inner(report[:i+1]+report[i+2:]):
                    return 1
                else:
                    # print("unsafe_2")
                    return 0
            else:
                if is_safe_inner(report[:i]+report[i+1:]) or is_safe_inner(report[:i+1]) :
                    return 1
                else: 
                    # print("unsafe_2")
                    return 0
    # print('safe')
    return 1


def is_safe_inner(report):
    is_incr = None
    for i in range(len(report)-1):
        a = report[i]
        b = report[i+1]
        if a>b:
            if a>b and is_incr==None:
                is_incr=False
            elif a>b and is_incr==False:
                is_incr = False
            elif a>b and is_incr==True:
                # print('unsafe')
                return 0
        elif a<b:
            if a<b and is_incr == None:
                is_incr = True
            elif a<b and is_incr == True:
                is_incr = True
            elif a<b and is_incr==False:
                # print('unsafe')
                return 0
        
        
        diff = abs(a-b)
        if diff <1 or diff>3:
            # print('unsafe')
            return 0
    # print('safe')
    return 1

n_safe = 0
for rep in inp:
    safer = is_safe(rep) 
    if safer == 1:
        print(rep)
        n_safe+=safer

print(n_safe)


new_checker = [[12, 10, 11, 13, 15, 18, 20], [1,2,3,5,4, 6], [44,9, 7,6,5,4], [56, 59, 58, 55, 53, 51, 49, 48]]
print("""

""")
for i in new_checker:
    print(i, is_safe(i))

m = [1,2,3,4,4]
print(m[:0]+m[1:])