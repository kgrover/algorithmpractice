# Author: Kshitij Grover
# Longest Increasing Subsequence

test_arr_1 = [1, 3, 5, 4, 6, 9, 15, 3, 1, 10, 13, 15, 19]
test_arr_2 = [5, 6, 7, 9]
test_arr_3 = []
test_arr_4 = [0, 0, 0]
test_arr_5 = [1, 2, 3, 0]

        
def get_lis(arr):
    if(len(arr) == 0):
        return -1
    
    # keeps track of max length found so far
    max_length = 0
    # length of current sequence, 1 because 
    # we start after the first element. 
    length_so_far = 1
    
    for i in range (1, len(arr)):
        if (arr[i] > arr[i-1]):
            length_so_far += 1
        else:
            length_so_far = 0
    
        if (length_so_far > max_length):
            max_length = length_so_far
            
    return max(max_length, 1)

print get_lis(test_arr_1)
print get_lis(test_arr_2)
print get_lis(test_arr_3)
print get_lis(test_arr_4)
print get_lis(test_arr_5)
