#!/usr/bin/python3

from random import randint

# Make a random list
values = []
for i in range(10):
    values.append(randint(0,10000))

print('A random list of values')
print(values)

# Bubble Sort
# The larger values 'bubble ups' the list until it is sorted, big oh of n^2
# Encourage you to look it up!

for i in range(1, len(values) - 1):
    for j in range(len(values) - i):
        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]    # swap values

print('\nIn order from smallest to biggest')
print(values)
