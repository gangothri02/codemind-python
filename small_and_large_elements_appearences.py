s=input()
mi=123
ma=0
for i in s:
    if i==" ":
        continue
    if ord(i)<mi:
        mi=ord(i)
    if ord(i)>ma:
        ma=ord(i)
a=chr(ma)
b=chr(mi)
print(b,s.count(b),a,s.count(a))
        