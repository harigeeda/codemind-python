a=input()
s=[]
if "a" not in a:
    s.append("a")
if "e" not in a:
    s.append("e")
if "i" not in a:
    s.append("i")
if "o" not in a:
    s.append("o")
if "u" not in a:
    s.append("u")
if len(s)>0:
    print(*(s))
else:
    print("0")