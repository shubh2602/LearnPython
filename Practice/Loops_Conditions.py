# Practice questions on loops and conditions

# Exercise 1: Print first 10 natural numbers using while loop

i = 1
while i <= 10:
    print(i)
    i = i+1

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

# Exercise 3: Calculate sum of all numbers from 1 to a given number

x = int(input("Enter a no. - "))
s = 0
for i in range(1, x + 1):
    s = s + i
print(s)

# Exercise 4: Print multiplication table of a given number

x = int(input("Enter the no. - "))
for i in range(1, 11):
    print(x, '*', i, '=', x * i)

# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
# sol1
for i in numbers:
    if i == 75 or i == 150 or i == 145:
        print(i)
# sol2
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)

# Exercise 7: Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

x = 5
for i in range(1, 6):
    for j in range(x, 0, -1):
        print(j, end=' ')
    x = x - 1
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
for i in range(4, -1, -1):
    print(list1[i])


