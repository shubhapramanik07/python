num = [2,3,5,7,11,13,17,19,3,19,3,7,2,3,1,11,1,17]

#freq_map = {}   
freq_map = dict() #we can also use this

for i in range(0,len(num)):
    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
        

# print(freq_map)
#**************************************************
# time_complexity: O(n)
# space_complexity: O(n)
#**************************************************


# 2nd _ method:
num = [2,3,5,7,11,13,17,19,3,19,3,7,2,3,1,11,1,17]
n = len (num)
hash_map = {}

for i in range (0,n):
    hash_map[num[i]] = hash_map.get(num[i],0) + 1

print(hash_map)

#**************************************************

#     in this question, we are using a dictionary to store the frequency of each element in the array.and the space complexity is O(n) because in the worst case, all elements are distinct and we have to store all of them in the dictionary.and the time complexity is O(n) because we are traversing the array once.
#**************************************************

# if the question is to find the frequency of a particular element in the array, then we can do it in O(1) time by using the dictionary.
