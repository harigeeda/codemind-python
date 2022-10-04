a=input()
s=0
b="1234567890"
for i in a:
    if i in b:
        s+=1
if s>0:
    print("Contains {} digit".format(s))
else:
    print("Doesn't contain digit")