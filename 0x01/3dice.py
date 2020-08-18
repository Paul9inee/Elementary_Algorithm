a, b, c = map(int, input().split())
list = [a,b,c]
list.sort()
if a == b and b == c and c ==a:
    print(10000 + a * 1000)
elif list[0] == list[1] or list[1] == list[2]:
    print(1000 + list[1] * 100)
else:
    print(list[2]*100)