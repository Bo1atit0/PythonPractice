"""
"""

name1 = input("Input Your Name: ")
name2 = input("Input Name Of Your Crush: ")
names = name1 + name2
res = 0
res2 = 0

for i in names:
    for j in "true":
        if i == j:
            res += 1
    for k in "love":
        if i == k:
            res2 += 1

result = str(res) + str(res2)
score = int(result)

if score > 90:
    print("Your Score is: {}".format(score))
    print("Your Are Compatible!!")
elif score >= 50 and score <= 90:
    print("Your Score is: {}".format(score))
    print("You are alright together")
elif score >= 0 and score < 50:
    print("Your Score is: {}".format(score))
    print("You are not compatible!!")
