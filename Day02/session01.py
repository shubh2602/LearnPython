import keyword

print(keyword.kwlist)

# out = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# keywords can't be used as variables

age = 7
age = age + 1
print(age)
age = 45
print(age * 2, "is the product of 45*2")

# Q - table of 2 with just print statement
x=int(input("enter the number"))
print(x, "* 1 = ", x*1)
print(x, "* 2 = ", x*2)
print(x, "* 3 = ", x*3)
print(x, "* 4 = ", x*4)
print(x, "* 5 = ", x*5)

x=int(input("enter the number"))
print(f"{x} * 1 = {x * 1}")
print(f"{x} * 2 = {x * 2}")
print(f"{x} * 3 = {x * 3}")
print(f"{x} * 4 = {x * 4}")
print(f"{x} * 5 = {x * 5}")

a, b, c = 1, 2.56, "shubham"
print(a)
print(b)
print(c)

print(type(a), a)
print(type(b), b)
print(type(c), c)

print(len(c), c[0])
print(len(c), c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6])

# add two no. from user input

x = int(input("enter 1st number"))
y = int(input("enter 2nd number"))
print(x + y)

x = input("enter 1st number")
y = input("enter 2nd number")
print("sum is ", int(x) + int(y))
