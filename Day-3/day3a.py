print("Welcome to teasure park")
a=input(print("Please Enter left or right: "))
if a=="left":
    b=input("Enter swim or wait? ")
    if b=="wait":
        c=input("Which door Red Blue Yellow?")
        if c=="yellow":
            print("You win !!")
        else:
            print("Game over")    
    else:
        print("Game over !!")    
else:
    print("Game over !! ") 
