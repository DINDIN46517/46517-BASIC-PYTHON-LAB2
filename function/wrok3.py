def show_table(n, limit):
    i = 1
    while i <= limit:
        print(n, "x", i, "=", n * i)
        i += 1

while True:
    n = int(input("Enter n: "))
    if n > 0:
        break

while True:
    limit = int(input("Enter limit: "))
    if limit > 0:
        break

show_table(n, limit)
