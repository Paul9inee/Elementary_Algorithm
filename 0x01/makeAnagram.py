A = list(input())
B = list(input())
count = 0
intersection = set(A) & set(B)
symmetric_difference = set(A) ^ set(B)

for x in symmetric_difference:
    count += A.count(x) + B.count(x)
for x in intersection:
    count += abs(A.count(x) - B.count(x))
print(count)