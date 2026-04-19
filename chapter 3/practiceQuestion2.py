# Write a Python Program that takes favorite food as input and prints:
# 1. The Middle 3 Characters
# 2. The last 2 Characters
str1 = input("Enter Your Favorite Food: ")
length = len(str1)
print("Middle 3 Characters: ",str1[length//2-1:length//2+2])
print("Last 2 Characters: ",str1[length-2:length])