# Q1 - LIST CREATION

# a. Create a list with five integer elements
age_list = [24, 25, 26, 27, 28]

# b. Create a list with five string elements
name_list = ["Anu", "Meera", "Sara", "Diya", "Riya"]

print(age_list)
print(name_list)

# Q2 - LIST OPERATIONS

# a. Append Yazhini to name_list
name_list.append("Yazhini")
print(name_list)

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print(age_list)

# c. Remove Yazhini from name_list
name_list.remove("Yazhini")
print(name_list)

# d. Pop the last element from age_list
age_list.pop()
print(age_list)

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])
print(age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print(age_list)

# g. Find maximum, minimum and sum
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

# Q3 - ACCESSING LIST ELEMENTS

# a. Print the first element
print(name_list[0])

# b. Print the last element
print(name_list[-1])

# c. Print elements from index 2 to index 4
print(name_list[2:5])

# d. Print the elements in reverse order
print(name_list[::-1])

# Q4 - DICTIONARIES

# a. Create a dictionary with five students and their marks
student_marks = {
    "Anu": 75,
    "Meera": 90,
    "Sara": 68,
    "Diya": 85,
    "Riya": 78
}

# b. Access and print the mark of a specific student
print(student_marks["Meera"])

# c. Add a new student Janani with mark 80
student_marks["Janani"] = 80
print(student_marks)

# d. Update an older student's mark to 82
student_marks["Anu"] = 82
print(student_marks)

# e. Print keys, values and items
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

# Q5 - SETS

# a. Create a set with the given values
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print(my_set)

# b. Attempt to change a set value
# my_set[4] = 's'
# Explanation:
# This gives a TypeError because sets are unordered
# and their elements cannot be accessed or modified using an index.

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Find union and intersection
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# Q6 - CONDITIONAL STATEMENTS

score = int(input("Enter your score (0 to 10): "))

if score > 7:
    print("Above Average: Excellent work! Keep it up!")

elif score >= 4:
    print("Average: Good effort! Keep practicing.")

else:
    print("Below Average: Keep practicing. You can improve!")
