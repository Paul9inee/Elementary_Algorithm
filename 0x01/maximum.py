list = []
for i in range(9):
    a = int(input())
    list.append(a)
ans = max(list)
print(ans)
print(list.index(ans)+1)