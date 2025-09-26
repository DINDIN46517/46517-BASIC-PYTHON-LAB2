nums = [10, 20, 30, 40]
total = sum(nums)
avg = total / len(nums)

with open("result.txt", "w") as f:
    f.write(f"รวม = {total}\n")
    f.write(f"ค่าเฉลี่ย = {avg:.2f}\n")
