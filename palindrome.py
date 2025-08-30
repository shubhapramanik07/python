num = 12357321
n = num
num1 = 0


# def is_palindrome(n):
#     original = n
#     num1 = 0
while n > 0:
        dig = n % 10
        num1 = (num1 * 10) + dig
        n //= 10
if num1 == num:
     print("palindrome!!")
else:
     print("not palindrome")
     

##time_compexity will be O(log10 n)


# is_palindrome(n)