import math
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, -5, -9]

# Example for loop solution to add 1 to each number in the list

numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

print('\n\nExercise 1:')
upp_fruits = [upper.upper() for upper in fruits]
print(upp_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

print('\n\nExercise 2:')
capitalized_fruits = [l.capitalize() for l in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

print('\n\nExercise 3:')
fruits_with_more_than_two_vowels = [char for char in fruits if char.count(
    'a') + char.count('e') + char.count('i') + char.count('o') + char.count('u') > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

print('\n\nExercise 4:')
fruits_with_only_two_vowels = [char for char in fruits if char.count(
    'a') + char.count('e') + char.count('i') + char.count('o') + char.count('u') == 2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

print('\n\nExercise 5:')
more_5 = [word for word in fruits if len(word) > 5]
print(more_5)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

print('\n\nExercises 6:')
equal_5 = [word for word in fruits if len(word) == 5]
print(equal_5)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

print('\n\nExercises 7:')
less_5 = [word for word in fruits if len(word) < 5]
print(less_5)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

print('\n\nExercise 8:')
number_characters = [len(word) for word in fruits]
print(number_characters)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

print('\n\nExercise 9:')
fruits_with_letter_a = [word for word in fruits if 'a' in word]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers

print('\n\nExercise 10:')
even_numbers = [even for even in numbers if even % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

print('\n\nExercise 11:')
odd_numbers = [odd for odd in numbers if odd % 2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

print('\n\nExercise 12:')
positive_numbers = [positive for positive in numbers if positive > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

print('\n\nExercise 13:')
negative_numbers = [negative for negative in numbers if negative < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

print('\n\nExercise 14:')
more_2_numerals = [more_2 for more_2 in numbers if len(str(more_2)) >= 2]
print(more_2_numerals)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

print('\n\nExercise 15:')
numbers_squared = [squared for squared in positive_numbers if (
    int(squared**(1/2))**2) == squared]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

print('\n\nExercise 16:')
odd_negative_numbers = [nums for nums in numbers if nums < 0 and nums % 2 != 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

print('\n\nExercise 17:')
numbers_plus_5 = [plus5+5 for plus5 in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

print('\n\nExercise BONUS:')


def isPrime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


primes = [num for num in numbers if isPrime(num) == True]
print(primes)
