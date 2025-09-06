n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

count = 0
for x in lst:
    if x > 50:
        count += 1

print("จำนวนที่มากกว่า 50:", count)
