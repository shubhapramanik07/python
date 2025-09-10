# str = "hey i am shubha"


# print(str[: :-1])

# ******************************

# s = "NITIN"

# def pal(s,l,r):
#     if l>=r:
#         print("palindrome")
#         return
#     elif s[l] == s[r]:
#         pal(s, l+1, r-1)   # recursive call here
#     else:
#         print("not a palindrome")
#         return


# r = len(s)
# pal(s,0,r-1)

# print(s)

# space complexity is O(n) due to call stack
# time complexity is O(n)
# ******************************

#* using recursion to check palindrome



# def is_palindrome(s,l,r):
#     if l>=r:
#         return True
#     if s[l] != s[r]:
#         return False
#     return is_palindrome(s, l+1, r-1)   # recursive call here
# s = "NITIN"
# r = len(s)
# print(is_palindrome(s, 0, r-1))


# ******************************

# s = "NeitaITIN"

# n = len (s)
# l = 0
# r = n-1

# while l<r:
#     if s[l]!=s[r]:
#         if s[l].lower() != s[r].lower():
#             print("not a palindrome")
#             break
#     l += 1
#     r -= 1
# else:
#     print("palindrome")
