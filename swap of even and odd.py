a=input()
s=list(a)
j=0
for i in range(2):
    temp=s[j]
    s[j]=s[j+1]
    s[j+1]=temp
    j=i+2

print("".join(s))