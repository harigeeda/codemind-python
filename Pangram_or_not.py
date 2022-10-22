a=input()
a=a.lower()
k=[]
c="qwertyuioplkjhgfdsazxcvbnm"
for i in a:
    if i in c:
        if i not in k:
            k.append(i)
print(len(k)>=26)