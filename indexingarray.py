"""from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])
#negative index
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])
#modifing index
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)
#index array
from array import array
arr=array('i',[10,20,30])
print(arr[5])"""
"""#slicing array
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])"""
"""#slicing with step
from array import array
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])"""
"""#negative slicing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])"""
"""#reverse array
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::-1])"""
#modifing slices
from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[125,35,45,50])
print(arr)