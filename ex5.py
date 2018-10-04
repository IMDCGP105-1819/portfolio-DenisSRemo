
n=99
while n>0:
    print( str(n)+" bottles of beer on the wall,"+str(n)+ " bottles of beer. ")
    n=n-1
    print("take one down, pass it around,"+str(n)+" bottles of beer on the wall... ")
if(n==0):
  print( "more bottles of beer on the wall, no more bottles of beer.")
  n=99
  print("Go to the store and buy some more,"+str(n)+" bottles of beer on the wall... ")
  