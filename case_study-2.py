# Author: MEE 10/13/21

ia = input("Enter an investment amount" )
ir = input("Enter an interest rate" )
t = input("Enter the amount of time the investemnt will be compounded")
v = float(ia) * ((1 + float(ir) / 12) ** 12 * float(t))

print("The value of your investment will be" + str(v))
