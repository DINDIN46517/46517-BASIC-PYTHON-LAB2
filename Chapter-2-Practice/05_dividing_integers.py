egg = input("กรุณากรอกจำนวนไข่ทั้งหมด: ")
all_eggs = int(egg)

trays = all_eggs // 30 
remaining = all_eggs % 30     

print("Trays:", trays, "Remaining:", remaining)
