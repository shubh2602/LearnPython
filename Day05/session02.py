# Practice questions on loops and conditions

# Exercise 1: Print first 10 natural numbers using while loop

# i = 1
# while i <= 10:
#     print(i)
#     i = i+1

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(j, end="  ")
    print()
