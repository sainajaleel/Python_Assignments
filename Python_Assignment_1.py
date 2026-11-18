# Q1 - STRING CONCATENATION
str1 = "Hello "
name = input("Enter your Name: ")

result = str1 + name

print(result)

str3 = ", welcome to Python programming"

result = result + str3

print(result)

# Q2 - STRING SLICING AND INDEXING

# a. Print the first character
print(result[0])

# b. Print the last character
print(result[-1])

# c. Print the first 5 characters
print(result[:5])

# d. Print the last 11 characters
print(result[-11:])

# e. Print the string in reverse
print(result[::-1])

# f. Print the word Python
start = result.index("Python")
print(result[start:start+6])

# Q3 - STRING METHODS

strM = "Python beginner tutorial"

# a. Convert to uppercase
print(strM.upper())

# b. Convert to lowercase
print(strM.lower())

# c. Capitalize the first letter
print(strM.capitalize())

# d. Count occurrences of 't'
print(strM.count('t'))

# e. Replace Python with Machine Learning
print(strM.replace("Python", "Machine Learning"))

# Q4 - TUPLES

# a. Create two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# b. Concatenate the tuples
t_combine = t1 + t2
print(t_combine)

# c. Repeat the elements 3 times
print(t_combine * 3)

# d. Access the 3rd element
print(t_combine[2])

# e. Access the first three elements
print(t_combine[:3])

# f. Access the last three elements
print(t_combine[-3:])

