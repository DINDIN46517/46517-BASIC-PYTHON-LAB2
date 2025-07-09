day = int(input("Enter your day: "))

if day in (1, 2, 3, 4, 5):
    print("weekday")
elif day in (6, 7):
    print("weekend")
else:
    print("unknown")
