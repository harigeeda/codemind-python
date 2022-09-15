p,r,t=map(int,input().split())
a=p*(1+(r/100))**t # formula for calculating amount
ci=a-p+p
print("{:.2f}".format(ci))
