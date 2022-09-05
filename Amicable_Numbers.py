a=int(input())
b=int(input())
s=0
y=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        y+=j
if s==b and y==a:
    print("Amicable")
else:
    print("Not Amicable")
    