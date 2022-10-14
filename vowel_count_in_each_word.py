s=input()
s=s.split()
for i in s:
    c=0
    for j in i:
        if ord(j)<97:
            m=ord(j)+32
            if m==97 or m==101 or m==111 or m==105 or m==117:
                c+=1
        else:
            if ord(j)==97 or ord(j)==101 or ord(j)==111 or ord(j)==105 or ord(j)==117:
                c+=1
    print(c,end=" ")