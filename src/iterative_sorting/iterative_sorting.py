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
