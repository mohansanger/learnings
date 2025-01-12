import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    value=numpy.array(arr,float)
    r=value[::-1]
    print(r)
    
    
        

arr = input("Enter a list space seprated").strip().split(' ')
result = arrays(arr)
print(result)