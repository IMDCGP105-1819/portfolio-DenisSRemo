
import random
guesses=0
n=random.randint(0,100)
print(n)
while guesses<=10:
    x=int(input())
    if x==n:
        print("You guessed")
        break;
    else:
        if x>n:
            print("The number is lower than yours")
            guesses+=1
        else:
            if x<n:
                print("The number is higher than yours")
                guesses+=1

            else:
               if guesses==10:
                    print("Too many guesses.The number is "+n)
                    break
