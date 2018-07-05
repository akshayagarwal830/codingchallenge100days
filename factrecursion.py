n=int(input("enter a number"))
def fact(x):
    if(x>0):
            return( x * fact(x-1))
    else:
            return 1
print(fact(n))
            
