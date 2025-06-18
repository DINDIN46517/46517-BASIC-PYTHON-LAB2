bill = float(input("Enter the total bill : "))
tip_percent = float(input("Enter the tip percentage : "))
people = int(input("Enter the number of people : "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
amount_per_person = total_bill / people

print(f"\nEach person: {amount_per_person:.2f} baht")
