# from hello_world import chai

# chai("sabalabalaaa")

# string = str(input("enter a string:"))
# length = len(string)
# for i in range(0,length):    
#        count = 0   
#        for x in string:
#            if(string[i] ==x):
#             count += 1

# print(count)

# or

# input_str = "abdxbajsoojda"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("unique Char is : ", char)
#         break

# items = ["app", "nkk", "oyy", "app", "iku"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate:", item)
#         break
#     unique_item.add(item)
# print(unique_item)

import time

wt = 1
maxtime = 15
attempt = 0
while attempt < maxtime:
    print("Waiting for", wt,"sec  //", "Attempt", attempt, "completed")
    time.sleep(wt)
    wt*= 2
    attempt += 1
  