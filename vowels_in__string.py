s=input()
l=[]
for k in s:
    if k=='a' or k=='e' or k=='i' or k=='o' or k=='u' or k=='A' or k=='E' or k=='I' or k=='O' or k=='U':
        if k not in l:
            l.append(k)
            print(k,end=" ")