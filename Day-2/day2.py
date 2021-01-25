#This is our Day-2 final project
print("Welcome to tips calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percantage tip would you like to give? 10, 12, or 15? "))
bill_with_tip=(bill*tip)/100+bill
user=int(input("How many people to split the bill? "))
split_with_bill=round(bill_with_tip/user,2)
print(f"Each person should pay: {split_with_bill}")

