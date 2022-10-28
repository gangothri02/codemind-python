s=input()
s=s.split()
mi=0
ma=0
for i in s:
    i=str(i)
    a=0
    b=124
    for j in i:
        if ord(j)<b:
            b=ord(j)
        if ord(j)>a:
            a=ord(j)
    mi+=b
    ma+=a
print(ma-mi)