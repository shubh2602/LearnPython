# literals

name = "shubham"  # (identifiers) = (literals)
print(type(name))

human = ["kanha", "shubham", "raj", "vaibhav"]  # List
fruits = ("apple", "mango", "orange", "grapes")  # tuple
a = {"A": "karma", "B": "is", "C": "bitch"}  # dict.
vowels = {'a', 'e', 'i', 'o', 'u'}  # set
print(type(human))
print(type(fruits))
print(type(a))
print(type(vowels))
print(len(human))  # 4
print(human[0:3])  # ['kanha', 'shubham', 'raj']
print(vowels[1])  # error - sets do no support accessing elements using square brackets [] or slicing

# operators

a = 5
b = 10
c = 4
d = -3
print(+a)  # sum operator (can be ignored here)
print(-b)  # prints -10
print(a + d)  # 2
print(a / d)  # -1.6666666666666667
a1 = True
print(not a)  # False (prints inverse on True)

b1 = 6
print(~b1)  # binary op. -7

print(a is b)  # Identity op (prints False)
print(a is not b)  # True

# in case of list
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # Prints: False (coz they stored at different location)

a=1
b=0
print(a and b)   # 0
print(a or b)    # 1

a = 2
a += 5  # a=a+5
b = 3
b -= 2
a -= 3
print(a)  # 4
print(b)  # 1
print(a > b)  # False a=2, b=3
print(b >= a)  # true
print(a==b) # false

# calculate area of circle
rad = float(input("enter radius - "))
area = (3.14 * pow(rad, 2))
print("area of cirle is - ", float(area))
print(3.14 * (rad ** 2))  # 314
print(3.14 * rad * rad)

# output
# enter radius - 3.14
# area of cirle is -  30.959144000000002
