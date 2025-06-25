point = int(input ("point :" ))
midterm = int(input ("midterm point :" ))
final = int(input ("final point:"))
all = point+midterm+final
if(all >= 80 and all<=100):
    print("A")
elif(all >= 75 and all<=79):
    print("B+")
elif(all >=70 and all<=74):
    print("B")
elif(all >=65 and all<=69):
    print("C+")
elif(all >=60 and all<=64):
    print("C")
elif(all >=55 and all<=59):
    print("D+")
elif(all >=50 and all<=54):
    print("D")
elif(all >=0 and all<=49):
    print("F")