# Write a function named sum_to that accepts 
# a single integer, n, and returns the sum of the integers from 1 to n.

###########################--START--#########################

def sum_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_to(n-1)
n = int(input("Enter a number: "))
print(sum_to(n))

# I add prompt to enter a number and print the sum of the integers from 1 to n.

###########################--END--#########################

