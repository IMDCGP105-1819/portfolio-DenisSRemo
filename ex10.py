def division(x):
    if(x%3==0 and x%5==0):
        print("FizzBuzz")
    else:
        if(x%3==0):
            print("Fizz")
        else:
            if(x%5==0):
                print("Buzz")
            else:
                print(x)
high=int(input())
low=int(input())
for i in range(low,high):
    division(i)