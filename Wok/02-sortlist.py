n = int(input())

numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

print("ลิสต์เดิม:", numbers)

numbers.sort()

print("ลิสต์เรียงแล้ว:", numbers)

