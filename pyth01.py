import numpy as np
a=np.array([[2,3,4],[1,6,5]])
print("sum of the array is =",a.sum())
print("maximum of the array is =",a.max())
print("minimum of the array is =",a.min())  
print("average number of the array is =",np.average(a))
print("maximum of 1 colounm array is =",a.max(axis=1))
print("minimum of 1 colounm array is =",a.min(axis=1))

b=np.array([[2,5,6],[6,7,4]])
print("after adding two metrisies :",a+b)
print("after multiplying two metrisies :",a*b)
print("after subtraction two metrisies :",a-b)





