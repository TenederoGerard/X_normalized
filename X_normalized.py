import numpy as np

X= np.random.random ((5,5))
print ("Original Array: ")
print (X)

x= np.mean(X) 
sdev=np.std(X)
Z= ((X-x)/sdev)
print ("Normalized Array: ")
print (Z)




