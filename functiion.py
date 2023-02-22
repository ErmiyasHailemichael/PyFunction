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


###########################--END--#########################

# Write a function named largest that takes a list of numbers as an argument 
# and returns the largest number in that list.

###########################--START--#########################

def largest_in_list (list):
    largest = list[0]
    for number in list:
        if number > largest:
            largest = number
    return largest
# print(largest_in_list([1,2,4,0]))
# print(largest_in_list([10, 4, 2, 231, 91, 54]))
###########################--END--#########################


# Write a function named occurances that takes two string arguments as input
# and counts the number of occurances of the second string inside the first string.

###########################--START--#########################

def occurances(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count
# print(occurances("fleep floop", "e"))
# print(occurances("fleep floop", "p"))
# print(occurances("fleep floop", "ee"))
# print(occurances("fleep floop", "fe"))
###########################--END--#########################

# Write a function named product that takes an arbitrary number of numbers, multiplies them together,
# and returns the product. (HINT: Review your notes on *args).

###########################--START--#########################

def product(*args):
    total = 1
    for number in args:
        total *= number
    return total
# print(product(-1,4))
# print(product(2,5,5))
# print(product(4,0.5,5))
###########################--END--#########################