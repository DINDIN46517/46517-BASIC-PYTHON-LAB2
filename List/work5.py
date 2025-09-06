n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

even = []
odd = []
for x in lst:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("เลขคู่:", even)
print("เลขคี่:", odd)
