# Vowel & Consonant Counter – Count the number of vowels and consonants in a given string.
emptySpace = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowelCount = 0
consonantCount = 0

for char in emptySpace:
    if char.isalpha():
        if char in vowels:
            vowelCount += 1
        else:
            consonantCount += 1

print(f"Vowels: {vowelCount}")
print(f"Consonants: {consonantCount}")

