# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # for loop for i after cur_index
        for j in range(cur_index + 1, len(arr)):
            # check each i against smallest i 
            if arr[j] < arr[smallest_index]:
                # replace smallest w j
                smallest_index = j
            # incrememnt outer loop & swap 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)
    # compare the first pair of elements
    for i in range(n - 1):
        for j in range(n - i -1):
    #   if rhs is < lhs, swap
    # iterate through list & compare adj pairs
    # if 1 or more swaps, repeat
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]          
    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

def insertion_sort(arr):
    # if part of the arr is sorted
        # we can have an index to the first element that's unsorted
        first_unsorted_index = 1
        while first_unsorted_index < len(arr):
        # take the next unsorted element
            cur_element = arr[first_unsorted_index]
        # compare to each of the elements in the sorted arr going from biggest to smallest
            sorted_index = first_unsorted_index - 1
            while  sorted_index >= 0:
            # if sorted element > cur element, shift it 
                if arr[sorted_index] > cur_element: 
                    arr[sorted_index + 1] = arr[sorted_index]
                    # decrement sorted index
                    sorted_index = sorted_index - 1                   
                elif arr[sorted_index] < cur_element:
                    # we found the right place for it
                    arr[sorted_index + 1] = cur_element
                    # break
                # when we get to the end
                if sorted_index == 0:
                    arr[sorted_index] = cur_element
                    # decreement sorted index to keep looping backwards
                sorted_index = sorted_index - 1
                    # insert the current element into the array
                arr[sorted_index + 1] = cur_element


