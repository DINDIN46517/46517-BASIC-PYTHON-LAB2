s = input()
a = s[:len(s)//2].lower()
b = s[len(s)//2:].lower()

if a < b:
    print("A comes before B")
elif a > b:
    print("A comes after B")
else:
    print("A equals B")
