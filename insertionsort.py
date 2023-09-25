arr = [7, 6, 5, 4, 3, 2, 1]

def print_array(arr):
    # Use a list comprehension to convert each element to a string
    # and join them with ' & ' as the separator
    formatted_array = "    ".join(str(item) for item in arr)
    
    # Print the formatted array with '\\' at the end
    print(formatted_array + "\n\n")

# print_array(arr)
# for i in range(1, len(arr)):
#     j = i - 1
#     while j >= 0 and arr[j] > arr[j + 1]:
#         temp = arr[j]
#         arr[j] = arr[j + 1]
#         arr[j + 1] = temp
#         j -= 1
#         print_array(arr)

# print_array(arr)
def shellSort(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = int(n/2)
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
            print_array(arr)
        gap = int(gap / 2)
 
 
# Driver code to test above
arr = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
 
n = len(arr)
print ("Array before sorting:")
print_array(arr)
shellSort(arr)
 


