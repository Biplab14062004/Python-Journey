# Write a program that:
# Takes a sentence as input
# Converts in to lowercase
# Replaces all spaces " " with underscores "_"
# Prints the new string

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
print(sentence)
sentence = sentence.replace(" ", "_")
print(sentence)