rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")

# This code generates a right-angled triangle pattern using asterisks (*).
# The outer loop iterates through the number of rows, and the inner loop
# prints asterisks for each row. The `end=" "` argument ensures that the asterisks
# are printed on the same line with a space in between, and `print("\r")
# moves to the next line after each row is printed.

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

rows = 5
for j in range(1, rows + 1):
    print("* " * j)

# This code generates a right-angled triangle pattern using asterisks (*).
# The outer loop iterates through the number of rows, and for each row,
# it prints asterisks followed by a space. The `* j` syntax repeats the string "* "
# `j` times, creating the desired pattern. The `print` function automatically
# moves to the next line after printing each row.

# Output:
#         *
#       * *
#     * * *
#   * * * * 
# * * * * *

rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print("\r")

# This code generates an inverted right-angled triangle pattern using asterisks (*).
# The outer loop iterates from `rows + 1` down to 1, and
# the inner loop prints asterisks for each row. The `end=" "` argument ensures that
# the asterisks are printed on the same line with a space in between,
# and `print("\r")` moves to the next line after each row is printed.

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5
k = 2 * rows -2 
for i in range(rows, -1, -1):
    for j in range(k, 0, i):
        print("*", end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

# This code generates a diamond pattern using asterisks (*).
# The outer loop iterates from `rows` down to 0, and the inner loops
# print asterisks for each row. The first inner loop prints asterisks
# in decreasing order, while the second inner loop prints asterisks
# in increasing order. The `end=" "` argument ensures that the asterisks
# are printed on the same line with a space in between, and `print("")`
# moves to the next line after each row is printed.

# Output:
# * * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
