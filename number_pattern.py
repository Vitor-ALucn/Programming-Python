def contnum(n):
    num = 1

    for i in range (0, n):
        for  j in range(0, i + 1):
            print(num, end=" ")
            num = num + 1
        print("\r")

n = 5
contnum(n)

# This code generates a pattern of consecutive numbers in a triangular format.
# The function `contnum` takes an integer `n` as input and prints a pattern
# where each row contains consecutive numbers starting from 1.
# The first row has 1 number, the second row has 2 numbers, and so
# on, up to `n` rows.

# Output:
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15