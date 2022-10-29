s=input()
s=s.split()
for i in s:
    i=str(i)
    mi=123
    ma=0
    for j in i:
      if ord(j)<mi:
          mi=ord(j)
      if ord(j)>ma:
          ma=ord(j)
    a=chr(ma)
    b=chr(mi)
    print(b,a,end=" ")
        