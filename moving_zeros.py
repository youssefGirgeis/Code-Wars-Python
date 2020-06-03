
# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


#solution 1

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

# solution 2: using list comperhension 

def move_zeros2(array):
    non_zeros = [i for i in array if isinstance(i, bool) or i != 0]
    return non_zeros + [0]*(len(array) - len(non_zeros))

print(move_zeros2([0,1,2,0,1,0,1,0,3,0,1]))
print(move_zeros2([False,1,0,1,2,0,1,3,"a"]))