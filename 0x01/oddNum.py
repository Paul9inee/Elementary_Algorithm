list = []
o_list = []
for i in range(7):
    a = int(input())
    list.append(a)
for i in range(7):
    if list[i] % 2 != 0:
        o_list.append(list[i])
if len(o_list) > 0:
    print(sum(o_list))
    print(min(o_list))
else:
    print(-1)