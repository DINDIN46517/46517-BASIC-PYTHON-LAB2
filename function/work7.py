def main():
    numbers = []

    while True:
        s = input().strip()
        if s == "end":
            break
        try:
            numbers.append(float(s))
        except ValueError:
            continue

    if not numbers:
        print("ไม่มีข้อมูล")
    else:
        print("ค่าสูงสุด:", max(numbers))
        print("ค่าต่ำสุด:", min(numbers))


if __name__ == "__main__":
    main()
