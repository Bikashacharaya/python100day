print("welcome to treasure island\nyour mission is to find the treasure")
a = input("do u want to go "left" or "right" ?"
if a == "left":
    b = input("do u want to "swim" or "wait"?")
    if b == "wait":
        c = input("which door u prefer?"yellow","red","blue"?")
        if c == "yellow":
            print("u win")
        elif c == "red":
            print("game over")
        elif c == "blue":
            print("game over")
        else:
            print("exit game over")
    else:
        print("game over")
else:
    print("game over")