# 0,1,1,3,2,5,8,13,21,34,55,89,144

num = 40
l = 0
r = 1
sum = 0

def fib(num,l,r,sum):
    
    while r < num:
        
        sum = l + r
        l = r
        r = sum 
        print(sum)
        return fib(num,l,r,sum)
print("0")
print("1")
fib(num,l,r,sum)