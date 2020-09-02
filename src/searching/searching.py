def linear_search(arr, target):
    pass
    # Your code here
    # Loop trhought array
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    # compare values
    # if end of list reached, rtn i not found
    # else i++ & repeat until i found
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # check for empty []
    if arr is None: 
        return False
   
    # start = starting index of the subset of the arr we're searching in - Inclusive
    # end = end index of the subset - inclusive
    start = 0
    end = len(arr) - 1

    # High level algorithm: 
    while  start <= end: 
    # Start at middle
    # how do we get the midpoint?
    #   for the whole arr, it's (len(ar) / 2 - 1
    #   for a subset of the arry: (start + end) // 2    
        mid_index = (start + end) // 2
        mid_index = arr[mid_index]

    # Compare it to target
        if target == mid_index:    
            return mid_index     

    # if target is < middle value, go left
        if target < mid_index:
            end = mid_index - 1 # eliminate lhs

    # if target is > middle value, go right
        if target > mid_index:
        # set start = mid_index +1
            start = mid_index + 1   # elimnate rhs  

    # Repeat. Halving the BST until you either find the target or not
    # if not found:     
        # else: 
        #     return mid_index

    # Check if not found
    #   if subset has a 0 or - length
    # how do we represent the subset that we're searching in? 
    #   store start and end index in variables
    return -1  # not found

