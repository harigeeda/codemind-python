def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def pal(x):
    k=str(x)
    if k==k[::-1]:
        return True
    else:
        return False
l=int(input())
k=l+1
while True:
    if prime(k)==True and pal(k)==True:
        print(k)
        break
    else:
        k+=1
        
    