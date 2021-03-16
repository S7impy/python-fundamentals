'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
text = input("Enter your text here: ")
vowels = 0
vowel_counts = {}

for characters in text:
    if characters in "aeiouAEIOU":
        vowels += 1

text_lower = text.lower()
for vowel in "aeiou":
    count = text_lower.count(vowel)
    vowel_counts[vowel] = count

print(vowels)
print(vowel_counts)
