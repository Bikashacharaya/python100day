height = float(input("enter your height in m"))
weight = float(input("enter your weight in kg"))
bmi = round(weight/height**2,2)
if bmi < 18.5:
    print(f"your bmi is {bmi} and u r underwight" )
elif bmi < 25:
        print("you have normal weight")
elif bmi < 30:
        print("you are over wight")
else:
    print("you are obese")