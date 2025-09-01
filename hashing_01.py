# m = [1,2,3,3,4,3,9,10,1,0,7]
# n = [7,69,2,0,11,3,3,1,10]
# hash = {}

# for i in n:
#     if i in m:
#         hash[i] = hash.get(i, 0) + 1
#     else:
#         hash[i] = 0
# print(hash)



# time_complexity = O(n)
# space_complexity = O(n)

# **************************************************

m = [1,2,3,3,4,3,9,10,1,0,7]
n = [7,69,2,0,11,3,3,1,10]
hash_list = [0] * 11
for num in n:
    if 0 <= num < len(hash_list):
        hash_list[num] += 1
# print(hash_list)

for num in m:
    if num<1 or num>10:
        print(0)
    print(hash_list[num])


    # time_complexity = O(n+m)
    # space_complexity = O(1)

    # for this approach, we are using a fixed-size list (hash_list) to store the counts of elements from n. This means that the space used by hash_list does not grow with the size of the input lists m and n, but is instead constant (O(1)) because its size is determined by the range of possible values (0-10 in this case).
        
    # time complexity still remains O(n + m) because we still need to iterate through both lists once.