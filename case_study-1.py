# Author MEE 10/12/21
x1 = input("What is your first x cordinate ")
y1 = input("What is your first y cordinate ")
x2 = input("What is your second x cordinate ")
y2 = input("What is your second y cordinate ")

d = (int(x2) - (int(x1)**2 + int(y2) - int(y1)**2)**.5)

print(d)
