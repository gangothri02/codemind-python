s=input()
s=s.split()
m=s[::-1]
t=[]
u=[]
m=str(m)
for i in m:
    if i.islower():
        t.append(ord(i))
    elif i.isupper():
        u.append(ord(i))
min1=min(t)
min2=min(u)
if min1==min2+32 or min1<(min2+32):
    print(chr(min1))
elif min1>min2+32:
    print(chr(min2))
    