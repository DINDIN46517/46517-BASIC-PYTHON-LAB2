n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

in_range = []
for x in lst:
    if 10 <= x <= 50:
        in_range.append(x)

print("ค่าที่อยู่ในช่วง 10-50:", in_range)
