n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)
maximum = max(numbers)
minimum = min(numbers)

print("มากที่สุด:", maximum)
print("น้อยที่สุด:", minimum)
