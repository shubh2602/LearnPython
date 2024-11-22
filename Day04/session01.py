# Conditoonal statements

age = int(input("Enter your age - "))
if age > 18:
    print("your r adult now")
else:
    print("you r still under age")

# max of two no.
x = int(input("Enter 1st no. - "))
y = int(input("Enter 2nd no. - "))
if x > y:
    print("max is ",x)
else:
    print("max is ",y)

# max of three no.
x = float(input("Enter 1st no. - "))
y = float(input("Enter 2nd no. - "))
z = float(input("Enter 3rd no. - "))

if x > y and x > z:
    print("max is ", x)
elif y > x and y > z:
    print("max is ", y)
else:
    print("max is ", z)

# nested if
age = int(input("Enter your age - "))
if age >= 18:
    if age >= 24:
        print("you can go for a trip")
    else:
        print("wait for your age to be 24")
else:
    print("you r still under age")

# nested elif
age = int(input("Enter your age - "))
if age >= 18:
    if 24 <= age <= 26:
        print("you can go for a trip")
    elif age > 26:
        print("you can go for bigger trips")
    else:
        print("wait for your age to be 24")
else:
    print("you r still under age")
