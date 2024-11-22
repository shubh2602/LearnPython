# For Loops statements
# syntax - range (start, stop-1, jumps)

# for i in range (0,10):
#     print(i)

# for i in range (0,10,2):
#     print(i)

# i = 1
# while i > 0:
#     print("infinite loop triggers...")
#     i = i + 1

# i = 0
# while 0 <= i <= 5:
#     print(i)
#     i = i + 1

# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

# score = int(input("Enter your score - "))
# if 90 <= score <= 100:
#     print("Grade A")
# elif 80 <= score <= 89:
#     print("Grade B")
# elif 70 <= score <= 79:
#     print("Grade C")
# elif 60 <= score <= 69:
#     print("Grade D")
# else:
#     print("Grade F")

# break - to exit the loop

# for i in range(1, 100):
#     print(i)
#     if i == 10:
#         break
# print("end of loop")

# pass - to skip the step(condition)

# for i in range(1, 30):
#     if 5 <= i <= 10:
#         pass
#     else:
#         print(i)
# print("end of loop")

# continue - to continue the step(condition)
# print("odd no. are - ")
# for i in range(1, 30):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)
# print("end of loop")

# for i in range(1, 30):
#     if i % 2 == 0:
#         print("found even no.", i)
#         continue
#     else:
#         print(i)
# print("end of loop")

# factorial
# x=5
# 5*4*3*2*1=120

x = int(input("enter a no. - "))
fact = 1
if x < 0:
    print("fact. not possible")
elif x == 0:
    print("fact.->>", 1)
else:
    for i in range(1, x + 1):
        fact = fact*i
print("fact.->>", fact)
