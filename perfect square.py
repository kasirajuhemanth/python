import math
a,b=map(int,input().split())
prod=a*b
sq=int(math.sqrt(prod))
if(sq*sq==prod):
  print("yes")
else:
  print("no")
