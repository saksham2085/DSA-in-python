from array import *
val = array('i', [10, 20, 30, 40, 50,60])
for i in range(0,6):
    print(val[i],end=" ")

print("\n")
#for x in val:
#    print(x,end=" ")
print(val.typecode)    

#val.reverse()
for i in range(0,len(val)):
    print(val[i],end=" ")

#val.insert(1,50)
for i in range(0,len(val)):
    print(val[i],end=" ")

copyarray  = array(val.typecode,(x*2 for x in val))
for i in range(0,len(val)):
    print(copyarray[i],end=" ")