a=list(input())
for i in range(0,len(a)):
    if a[i]=="6":
        a[i]="9"
        break
print("".join(a))