l=input()
a=l.split()
d=list(map(int,a))
b=[ ]
for i  in d:
            if i not in b:
                        b.append(i)
for i in b:
            print(i, end=' ')
