## o(n) test - essentially worst case scenario for the run.

#o(n)
def print_test(n):
    for i in range(n):
        print(i)

#o(n^2)
def print_test_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

#o(log n)
def print_test_3(n):
    # start of function
    i = 1
    while i < n:
        # loop that runs while i is less than n
        print(i)
        # print the current value of i
        i *= 2
        # double the value of i each iteration            