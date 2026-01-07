from array import *

#val = array('i', [10, 20, 30, 40, 50,60,70,80,90])
#a = val[2:5]
arr = array('i',[])
n = int(input('enter a number'))
for i in range(0,n):
     arr.append(int(input('enter value')))
for x in arr:
    print(x,end=" ")            