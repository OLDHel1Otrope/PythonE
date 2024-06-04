# Define a function to square a number
def square(x):
    return x * x

# Apply the function to each element in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the map object to a list
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]


# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Apply the function to filter the list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list
even_numbers_list = list(even_numbers)
print(even_numbers_list)  # Output: [2, 4, 6]


from functools import reduce

# Define a function to add two numbers
def add(x, y):
    return x + y

# Apply the function cumulatively to the items of the list
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15
