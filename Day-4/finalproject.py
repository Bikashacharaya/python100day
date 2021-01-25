#RockPaperSessior
import random
print("--Welcome to Rock Paper Sessior Game--")
b=1
point=0
#condition Rock
while(b<=10):
  user=input("Enter any Rock Paper Sessior (R/P/S)? ")
  print(f"You select: {user}")
  bot=["R","P","S"]
  bot_select=random.choice(bot)
  print(f"Bot select: {bot_select}")
  b=b+1


  if user=="R" and bot_select=="P":
    print("You lost !")
    point=point-1
    print(f"Your Point: {point}")
  
  elif user=="R" and bot_select=="S":
    print("You win!")
    point=point+1
    print(f"Your Point: {point}")

  elif user=="R" and bot_select=="R":
    print("Game Draw!")
    print(f"Your Point: {point}")


#condition Paper

  if user=="P" and bot_select=="S":
    print("You lost !")
    point=point-1
    print(f"Your Point: {point}")
  
  elif user=="P" and bot_select=="R":
    print("You win!")
    point=point+1
    print(f"Your Point: {point}")

  elif user=="P" and bot_select=="P":
    print("Game Draw!")
    print(f"Your Point: {point}")


#conditon Sessior


  if user=="S" and bot_select=="R":
    print("You lost !")
    point=point-1
    print(f"Your Point: {point}")
  
  elif user=="S" and bot_select=="P":
    print("You win!")
    point=point+1
    print(f"Your Point: {point}")

  elif user=="S" and bot_select=="S":
    print("Game Draw!")
    print(f"Your Point: {point}")

print(f"Your Final Point : {point} ")
print("Thanks for playing with us!!")
