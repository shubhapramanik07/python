# arr = [2,31,2,6,8,9]
# print(arr[::-1])
#******************************************
# Q) reverse an array using recursion
#******************************************
arr = [2, 31, 2, 6, 8, 9]

def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)

def reverse(arr, start, end):
    reverse_array(arr, start, end)
    return arr

print(reverse(arr, 1, 2))  # reversing from index 1 to 5
# time complexity is O(n/2) = O(n)
# space complexity is O(n) due to call stack