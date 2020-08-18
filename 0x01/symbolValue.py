list = []
for i in range(5):
    a = int(input())
    list.append(a)
list.sort()
print(sum(list)//len(list))
print(list[2])