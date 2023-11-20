#simple method to calculate factorial
a=int(input('Enter number to calculate factorial:  '))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)

#with recursively calculate factorial..
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)


#to check zeroes in factorial
def traise(n):
    count=0
    while n%10 == 0:
        count+=1
        n=n/10
    return count

#to check zeroes in factorial in another method
def traiseZ(n):
    res=0
    for i in range(5,n+1,i*5):
        print(i)
        res=res+n/i
    return res
print(traiseZ(fact(15)))
print(traise(fact(15)))