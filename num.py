import numpy as np
def find_largest_smallest_number(numbers):
    arr=np.array(numbers)
    return np.max(arr),np.min(arr)

numbers=[56,89,4,87,78,1,100]
largest,smallest=find_largest_smallest_number(numbers)
print(f"largest {largest},smallest:{smallest}")    
