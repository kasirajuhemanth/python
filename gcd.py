a,b=map(int,input().split())
if(a<b):
 small=a
else:
 small=b
gcd=1
for i in range(1,small+1):
  if(a%i==0 and b%i==0):
     gcd=gcd*i
print(gcd)