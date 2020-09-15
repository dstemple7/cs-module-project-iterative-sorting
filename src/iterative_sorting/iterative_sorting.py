# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # capture variable to be swapped of the smallest_index
        # then reset the smallest index to be the now current index in the array
        # last set the current index in the array to be the swap variable
        swap = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = swap

    return arr

    # # Sean's solution code
    # def selection_sort(arr):
    #     # loop through n-1 elements
    #     for i in range(0, len(arr) - 1):
    #         smallest_index = i
    #         # TO-DO: find the smallest element
    #         # (hint, can do in 3 loc)
    #         # loop through every elem to the right of the boundary and keep track of the smallest elem
    #         # we've seen so far until we get to the end
    #         for j in range(i+1, len(arr)):
    #             if arr[j] < arr[smallest_index]:
    #                 smallest_index = j

    #         # TO-DO: swap
    #         arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
                # # under the hood, python is doing this
                # temp = arr[smallest_index]
                # arr[smallest_index] = arr[i]
                # arr[i] = temp

    #     return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # range sets the point to start & stop, sort of the boundaries
    # look through and see if each element is greater than the element to it's right on index position
    # if so, push the element to it's right and bring the element to it's right to the left one index position
    for i in range(1, len(arr)-1):
        for h in range(0, len(arr)-i):
            if arr[h] > arr[h+1]:
                swap = arr[h+1]
                arr[h+1] = arr[h]
                arr[h] = swap

    return arr

# # sean's solution code
# def bubble_sort(arr):
#     # keep a flag that tracks whether any swaps occurred
#     swaps_occurred = True
#     while swaps_occurred:
#         swaps_occurred = False
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swaps_occurred = True
#     return arr

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
    if len(arr) == 0:
        return arr
    
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    # loop through our arr
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # for each distinct arr value, increment arr[value] by 1
        buckets[value] += 1

    # at this point, our buckets array has all of the counts of every distinct value in our input array

    output = []
    # loop through our buckets arry
    # enumerate gives index as well as the bucket value
    for index, count in enumerate(buckets):
        # for the current count
        output.extend([index for i in range(count)])
        # add that many values to an output array

    return output

