num1=int(input())
sum1=0
while num1>0 or sum1>=10:
    if num1==0:
        num1=sum1
        sum1=0
    sum1+=(num1%10)**2
    num1=num1//10
if sum1==1 or sum1==7:
    print("True")
else:
    print("False")