"""
Compatibility Calculator Program

This program takes input names from the user, concatenates them, and then calculates a compatibility score based on the occurrences of the letters 't', 'r', 'u', 'e', 'l', 'o', 'v', and 'e' in the combined names. The program categorizes the compatibility into three levels: high, moderate, and low.

Usage:
1. Run the program.
2. Input your name when prompted.
3. Input the name of your crush when prompted.
4. The program calculates the compatibility score and provides a compatibility level.

Note: The compatibility score is calculated by counting the occurrences of the letters 't', 'r', 'u', 'e', 'l', 'o', 'v', and 'e' in the combined names.

"""

# Get input names from the user
name1 = input("Input Your Name: ")
name2 = input("Input Name Of Your Crush: ")

# Concatenate the names
names = name1 + name2

# Initialize counters for 'true' and 'love'
res = 0
res2 = 0

# Count occurrences of 'true' and 'love' in the combined names
for i in names:
    for j in "true":
        if i == j:
            res += 1
    for k in "love":
        if i == k:
            res2 += 1

# Combine the counters into a single result string and convert it to an integer
result = str(res) + str(res2)
score = int(result)

# Categorize compatibility based on the score
if score > 90:
    print("Your Score is: {}".format(score))
    print("You Are Compatible!!")
elif 50 <= score <= 90:
    print("Your Score is: {}".format(score))
    print("You are alright together")
elif 0 <= score < 50:
    print("Your Score is: {}".format(score))
    print("You are not compatible!!")
