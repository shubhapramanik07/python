#* in python an infinite recursion occurs when a function calls itself without a base case or termination condition, leading to a stack overflow error. to avoid infinite recursion, ensure that your recursive functions have a clear base case and that the input is modified in each recursive call to eventually reach that base case.

    #* here in python it calls itself by default limit of 987 times

#we are studying head recursion which means the recursive call is the first statement in the function. and tail recursion means the recursive call is the last statement in the function.




# from itertools import count
def func(count):
    # Head recursion
    if count == 4:
        return
    print("shubha")
    func(count + 1)


def func_tail(count):
    # Tail recursion
    if count == 4:
        return
    func_tail(count + 1)
    print("pramanik")


# Run both
print("Head Recursion Output:")
func(0)

print("\nTail Recursion Output:")
func_tail(0)

# i want to push it into github
