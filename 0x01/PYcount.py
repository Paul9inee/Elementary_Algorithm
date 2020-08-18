s = "pPoooyY"
count_p = 0
count_y = 0
for x in s:
    if x == "p":
        count_p +=1
    elif x == "P":
        count_p += 1
    elif x == "y":
        count_y += 1
    elif x == "Y":
        count_y += 1

if count_p == count_y:
    print