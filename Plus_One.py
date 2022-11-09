a=int(input())
b=list(map(int,input().split()))
s=''
for i in b:
    s+=str(i)
k=(int(s)+1)
for j in str(k):
    print(j,end=" ")
    
