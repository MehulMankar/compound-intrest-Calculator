principle =0
rate = 0
time = 0
while principle <=0:
  principle = float(input("Enter the priciple amount:  "))
  if principle <=0:
    print("The principle amount must be  greater than 0")
while rate <=0:
  rate = float(input("Enter the interest rate:  "))
  if rate <=0:
    print("The interest rate must be greater than 0")
while time <=0:
  time = float(input("Enter the time in years:  "))
  if time <=0:
    print("The time must be greater than 0")
compound_intrest = principle * (1 + rate/100) ** time
print("The compound intrest is:  ", compound_intrest)