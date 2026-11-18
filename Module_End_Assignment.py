# STEP 1 - PRELOADED FEEDBACKS

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '   Very GOOD Service!!!',
        'poor support,        not happy   ',
        'GREAT experience! will come again.',
        'okay     okay...',
        '   not    BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# STEP 2 - ADD NEW FEEDBACKS

number = int(input("How many feedbacks do you want to add? "))

for i in range(number):

    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")
    rating = int(input("Enter your rating (1-5): "))

    feedback_data['S_No'].append(i + 11)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nUpdated Feedback Data:")
print(feedback_data)

# STEP 3 - TEXT CLEANING

for i in range(len(feedback_data['Feedback'])):

    feedback = feedback_data['Feedback'][i]

    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")

    feedback = " ".join(feedback.split())

    feedback = feedback.lower()

    feedback_data['Feedback'][i] = feedback

print("\nCleaned Feedback:")
print(feedback_data['Feedback'])

# STEP 4 - WORD COUNT INSIGHTS

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        if word.lower() in feedback.split():
            count = count + 1

    return count


print("Good:", count_word_in_feedbacks("good"))
print("Poor:", count_word_in_feedbacks("poor"))
print("Excellent:", count_word_in_feedbacks("excellent"))

# STEP 5 - FINAL SUMMARY & INSIGHTS

print("\nFinal Feedback Data:")
print(feedback_data)


# Average Rating

total = 0

for rating in feedback_data['Rating']:
    total = total + rating

average = total / len(feedback_data['Rating'])

print("\nAverage Rating:", average)

# Longest Feedback

longest = ""
max_words = 0

for feedback in feedback_data['Feedback']:
    count = len(feedback.split())

    if count > max_words:
        max_words = count
        longest = feedback

print("Longest Feedback:", longest)
print("Word Count:", max_words)

# Unique Words

unique_words = []

for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        if word not in unique_words:
            unique_words.append(word)

print("\nUnique Words:")
print(unique_words)



