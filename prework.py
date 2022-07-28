# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the 
# function.

def hello_username():
    """Print simple message saying hello to username."""
    print('Please enter your username: ')
    user_name = input()
    print(f"hello_{user_name.upper()}!")

hello_username()

# Question 2:
# Write a Python function, first_odds that prints the odd numbers from 1-100
# and returns nothing.

def first_odds():
    """Print the odd numbers from 1-100."""
    for i in range (1,101):
        if i % 2 != 0:
            print(i)

first_odds()

# Question 3:
# Write a Python function, max_num_in_list to return the max number of a given
# list.

def max_num_in_list(a_list):
    """State the max number of any given list."""
    print(max(a_list))

# Examples:
a_list = [3, 10, 36, 14, 8] 
max_num_in_list(a_list)

a_list = [3.5, 122, 355.3, 3]
max_num_in_list(a_list)

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be a boolean Type (true/false).

def is_leap_year(a_year):
    """"Check to see if a given year is a leap year."""
    if (a_year % 4 == 0) and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

# Examples:
print(is_leap_year(2012))
print(is_leap_year(2019))
print(is_leap_year(1988))
print(is_leap_year(2000))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive 
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
# are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """Check if numbers in any given list are consecutive numbers."""
    
    for i in range(len(a_list)-1):
        if a_list[i] + 1 != a_list[i+1]:
            return False

    return True

# Examples:
a_list = [1,2,3,4,5,6]
print(is_consecutive(a_list))

a_list = [2,3,4,6]
print(is_consecutive(a_list))    