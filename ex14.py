def fibo(x):
    if x<2:
        return x
    return fibo(x-2)+fibo(x-1)
for i in range(25):
    print(fibo(i))
        

