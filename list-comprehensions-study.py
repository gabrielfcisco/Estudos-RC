# Pin-Pan Prank

a = ["pin-pan" if el % 2 == 0 and el % 3 == 0
     else "pin" if el % 2 == 0
     else "pan" if el % 3 == 0
     else el for el in range(1, 101)]

print(a)

# List of exercises solved from https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313

nums = [i for i in range(1, 1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# 1. Find all of the numbers from 1–1000 that are divisible by 8
ex1 = [i for i in nums if i % 8 == 0]
print(ex1)

# 2. Find all of the numbers from 1–1000 that have a 6 in them

ex2 = [i for i in nums if "6" in str(i)]
print(ex2)

# 3. Count the number of spaces in a string

ex3 = len([i for i in string if i == " "])
print(ex3)

# 4. Remove all of the vowels in a string

ex4 = [i for i in string if i != 'a' and i != 'e' and i != 'o' and i != 'u']
print(ex4)

# 5. Find all of the words in a string that are less than 5 letters

palavras = string.split(' ')
ex5 = [word for word in palavras if len(word) < 5]
print(ex5)

# 6. Use a dictionary comprehension to count the length of each word in a sentence

ex6 = {word: len(word) for word in palavras}
print(ex6)

# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)

ex7 = [num for num in nums if True in [
    True for divisor in range(2, 10) if num % divisor == 0]]

print(ex7)

# 8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

ex8 = {num: max([divisor for divisor in range(1, 10) if num %
                divisor == 0]) for num in nums}

print(ex8)
