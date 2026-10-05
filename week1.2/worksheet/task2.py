# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

nbr = read_numbers()

if not nbr:
    sys.exit("Error: no numbers provided")

n = len(nbr)
m = sum(nbr) / n
nbr.sort()

if not n % 2:
    med = (nbr[n // 2 - 1] + nbr[n // 2]) / 2
else:
    med = nbr[n // 2]

print(f"Minimum = {nbr[0]}")
print(f"Maximum = {nbr[-1]}")
print(f"Mean = {m}")
print(f"Median = {med}")


