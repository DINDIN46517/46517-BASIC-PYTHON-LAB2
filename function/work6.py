def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Exit")

        choice = input()

        if choice == "4":
            print("End")
            break

        if choice in ["1", "2", "3"]:
            a = float(input())
            b = float(input())

            if choice == "1":
                print(add(a, b))
            elif choice == "2":
                print(sub(a, b))
            elif choice == "3":
                print(mul(a, b))

if __name__ == "__main__":
    main()
