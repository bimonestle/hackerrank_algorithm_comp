# This is a staircase of size n = 4:
# ooox
# ooxx
# oxxx
# xxxx

# Its base and height are both equal to n.
# It is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.

# Write a program that prints a staircase of size n.
# Print a staircase as described above.


def staircase(n):
    last = n+1
    for idx in range(1, last):
        if idx < last:
            print(" " * (n-idx) + "#" * idx)