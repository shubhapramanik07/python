m = [1,2,3,3,4,3,9,10,1,0,7]
n = [7,69,2,0,11,3,3,1,10]
hash = {}

for i in n:
    if i in m:
        hash[i] = hash.get(i, 0) + 1
    else:
        hash[i] = 0
print(hash)







#bhawaiya - nihar adhikary...

# time_complexity = O(n)
# space_complexity = O(n)