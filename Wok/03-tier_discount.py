amount = float(input("input your shipped cost: "))

if amount > 2000:
    discount_rate = 0.15
elif amount > 1000:
    discount_rate = 0.10
elif amount > 500:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discount = amount * discount_rate
net_price = amount - discount

print(f"ส่วนลด: {discount:.2f} บาท")
print(f"ราคาสุทธิ: {net_price:.2f} บาท")
