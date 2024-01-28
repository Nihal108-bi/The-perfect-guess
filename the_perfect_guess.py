'''We are going to write a program that generates
a random number and asks the user to guess it
if the player's guess is higher than the actual
number , the problem displays "lower  number plese"
similarly if the the user's guess is too low,the
programm prints"higher number plese"
when the user guess the correct number, the 
program displayes the number of guesses the player
used to arrive at the number.'''
import random
randnumber= random.randint(1,100)
guesses=0
userguess=None

while(userguess != randnumber):
    userguess=int(input("enter your guess:"))
    guesses+=1
    if(userguess==randnumber):
       print("You guess it right!")
    else:
       if(userguess>randnumber):
          print("you guessed it wrong! Enter a smaller number")
       else:
           print("you guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
   hiscore=int(f.read())
   
if(guesses<hiscore):
   print("you have just broken the high score!")   
   with open("hiscore.txt","w") as f:
      f.write(str(guesses))
       