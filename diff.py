l1=[ 1,2,3,4,5]
l2=[ 1,2,6,7,8]
l=[l1.append(i) for i in l2 if i not in l1]
l4=[i for i in l2 if i in l1]
lst= l[ ] -l4[ ]
print(lst)
