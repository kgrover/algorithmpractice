# Longest Increasing Subsequence

test_arr_1 = [1, 3, 5, 4, 6, 9, 15, 3, 1, 10, 13, 15, 19]
test_arr_2 = [5, 6, 7, 9]
test_arr_3 = []
test_arr_4 = [0, 0, 0]
test_arr_5 = [1, 2, 3, 0]

# DP O(n^2) solution
def get_lis_dp(arr):
    
    lis = [1] * len(arr)
    
    for i in range (0, len(arr)):
        for j in range(0, i):
            if (arr[i] > arr[j]):
                if (lis[i] < lis[j] + 1):
                    lis[i] = lis[j] + 1
        
    max_lis = 1
    for index in range (0, len(lis)):
        if (lis[index] > max_lis):
            max_lis = lis[index]
    
    return max_lis

    


print get_lis_dp(test_arr_1)
print get_lis_dp(test_arr_2)
print get_lis_dp(test_arr_3)
print get_lis_dp(test_arr_4)
print get_lis_dp(test_arr_5)
