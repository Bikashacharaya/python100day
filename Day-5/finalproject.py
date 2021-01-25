import random

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','S','T','U','V','W','X','Y','Z']
digit=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*']

letter_ran=int(input("Enter letter how many you like? "))
digit_ran=int(input("Enter digit how many you like? "))
symbol_ran=int(input("Enter symbol how many you like? "))
password=""
for char in range(1,letter_ran+1):
    password+=random.choice(letter)
for char in range(1,digit_ran+1):
    password+=random.choice(digit)
for char in range(1,symbol_ran+1):
    password+=random.choice(symbol)
# suffle_pass=random.shuffle(password)
#print(f"Your password {password}")
print(f"Your password {password}")
# random.shuffle(password)
# print(password)
