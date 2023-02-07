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

# Write a function named largestthat takes a list of numbers as an argument 
# and returns the largest number in that list.

###########################--START--#########################

def largest(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number 
    return largest_number
enter_numbers = input("Enter a list of numbers: ")
numbers = enter_numbers.split()
print(largest(numbers))
print('The largest number is: ', largest(numbers))

###########################--END--#########################


# Write a function named occurances that takes two string arguments as input
# and counts the number of occurances of the second string inside the first string.

###########################--START--#########################

def occurances(string, string2):
    count = 0
    for i in range(len(string)):
        if string[i] == string2:
            count += 1
    return count
string = input("Enter a string: ")
string2 = input("Enter a string2: ")

result = occurances(string, string2)

print("The number of occurances of the second string inside the first string is: ", result)

###########################--END--#########################

# Write a function named product that takes an arbitrary number of numbers, multiplies them together,
# and returns the product. (HINT: Review your notes on *args).

###########################--START--#########################

def product(*args):
    result = 1
    for number in args:
        result *= number
    return result
args = input("Enter a list of numbers: ")

result = product(args)
print('The product of the numbers is: ', result)

###########################--END--#########################