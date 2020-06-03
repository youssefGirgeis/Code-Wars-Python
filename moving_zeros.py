
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


#solution

def move_zeros(array):
    result = []
    zeros = []
    non_zeros = []

    for value in array:
        if value == 0 or value == 0.0:
            if type(value) == int or type(value) == float:
                zeros.append(value)
            else:
                non_zeros.append(value)
        else:
            non_zeros.append(value)
    result = non_zeros + zeros   
    return result

print(move_zeros([0,1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
