num = 1235321
n = num
num1 = 0


def is_palindrome(n):
    original = n
    num1 = 0
    while n > 0:
        dig = n % 10
        num1 = (num1 * 10) + dig
        n //= 10
    if num1 == original:
        print("palindrome!!")
    else:
        print("not palindrome")
     
is_palindrome(n)