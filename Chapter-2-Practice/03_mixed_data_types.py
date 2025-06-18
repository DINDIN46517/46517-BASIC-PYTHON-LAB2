product = input("Product: ")
price = input("Price: ")

x = float(price)  
new_price = ('{:.10f}'.format(x)).rstrip('0').rstrip('.') 

print("Product:", product, ", Price:", new_price, "THB")
