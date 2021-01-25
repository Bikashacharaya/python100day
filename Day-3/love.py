#lovecalculator
print("Welcome to love calculator")
male=input("Enter his name? ")
female=input("Enter her name? ")

#combined two string

combined_string=male+female
lower_string=combined_string.lower()


#countstrings

t=lower_string.count('t')
r=lower_string.count('r')
u=lower_string.count('u')
e=lower_string.count('e')

l=lower_string.count('l')
o=lower_string.count('o')
v=lower_string.count('v')
e=lower_string.count('e')

true_count=int(t+r+u+e)
love_count=int(l+o+v+e)

str_true=str(true_count)
str_love=str(love_count)

love_score=str(str_true+str_love)

#convert string into int 

lovescore=int(love_score)

#condition statement

if lovescore<10:
    print(f"Your score is {lovescore}, you go together like coke and mentos :p")

elif lovescore in range(40,76):
    print(f"Your score is {lovescore}, you are alright together :D")

elif lovescore>76:
    print(f"Your score is {lovescore}, you both are made for each other ;)") 

else:
    print("Try again !!")    




