
### Problem
#---------

# You are going to be given an array of integers. Your job is to take that array and
# find an index N where the sum of the integers to the left of N is equal to the sum of the integers
#  to the right of N. If there is no index that would make this happen, return -1.

### Solution
#-----------

def find_even_index(arr):
    left_list = []
    right_list = []
    result = -1

    for index in range(len(arr)):
        left_list = arr[:index]
        right_list = arr[index+1:]

        if sum(left_list) == sum(right_list):
            result = index
            break 
        
    return result


### Test

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))
print(find_even_index(list(range(1,100))))
print(find_even_index([0,0,0,0,0]))
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
print(find_even_index(list(range(-100,-1))))
