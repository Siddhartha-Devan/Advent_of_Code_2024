with open ('samp_inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")

# print(inp)

rules = inp[:inp.index("")]
updates = inp[inp.index("")+1:]
rules = [i.split("|") for i in rules]
updates = [i.split(",") for i in updates]

for i in range(len(rules)):
    rules[i] = [int(j) for j in rules[i]]

for i in range(len(updates)):
    updates[i] = [int(j) for j in updates[i]]

# print(rules)
# print(updates)

crct_updates = []
wrng_updates = []

for i in range(len(updates)):
    upd = updates[i]
    applicable_rules = []
    for page in upd:
        for r in rules:
            if page in r:
                # print(i, r)
                applicable_rules.append(r)
    appl_r = []
    for r in applicable_rules:
        if r[0] in upd and r[1] in upd:
            # print(r)
            appl_r.append(r)
    
    upd_val = True
    for ii in range(len(upd)):
        ith_page = upd[ii]
        page_irukka_rules = []
        for r in appl_r:
            if ith_page in r:
                page_irukka_rules.append(r)
        # print(ith_page, page_irukka_rules)

        munnadi_pages = []
        pinnadi_pages = []
        for r in page_irukka_rules:
            if r[0] == ith_page:
                pinnadi_pages.append(r[1])
            if r[1] == ith_page:
                munnadi_pages.append(r[0])
        
        # print(ith_page, page_irukka_rules)
        # print(munnadi_pages, pinnadi_pages)

        next_pages = upd[ii+1:]
        prev_pages = upd[:ii]
        # print(prev_pages, next_pages)
        
        for p in prev_pages:
            if p in pinnadi_pages:
                print("update not valid: ", p, pinnadi_pages)
                upd_val = False
                break
        
        for p in next_pages:
            if p in munnadi_pages:
                print("update not valid: ", p, munnadi_pages)
                upd_val = False
                break
                
        if upd_val == False:
            print(upd, "falsed_naduvula")
            break

    if upd_val:
        print("valid", upd)
        crct_updates.append(upd)
        
        

    
# print(crct_updates)
mid_sum = 0
for i in range(len(crct_updates)):
    c_upd = crct_updates[i]
    mid_sum+=c_upd[len(c_upd)//2]

print("mid_sum: ", mid_sum)