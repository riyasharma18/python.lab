t=(1,1,2,3,4,5,5,6)
b=[ ]
for i in t:
      if t.count(i)>1 and i not in b:
             print(i)
             b.append(i)

