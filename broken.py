import random

print("Think of a number between 1 and 10")
answer = ""
while answer != "y"
    print("Is " + str(random.randint(1, 10)) + " your number? ('y' for yes, any key for no)")
    answer = input()
print("I guessed your number!")
# the p was capitalized
