# Write a Python Program that takes any word or Sentence as input and prints:
# The First character of the word/sentence
# The Last character of the word/sentence
# The Total Number of Characters in the word/sentence

sentence = input("Enter a word or sentence: ")
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Total number of characters:", len(sentence))