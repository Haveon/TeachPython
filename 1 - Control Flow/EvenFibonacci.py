#!/usr/bin/python3

evenFibonaccis = []    # Use to store our values
a_old = 1    # Fibonacci starts with 1, 1
a_new = 1

while len(evenFibonaccis)<100:   # Keep going until we have 100 numbers
    a_old, a_new = a_new, a_old + a_new   # make a_old into a_new and at the
                                          # same time make the new a_new
    if a_new%2 == 0:    # if a_new is evenly divisible by 2
        evenFibonaccis.append(a_new)    # add the number to our list

print(evenFibonaccis)
