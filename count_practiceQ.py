# This program counts the number
# February 21, 2020.

with open("MATH323_suggested_ex.txt", "r") as f:
    count = sum(line.count(",") for line in f)
    print(count)