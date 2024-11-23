# Patterns logic

# step1   layman approach
print("* * * *")
print("* * * *")
print("* * * *")
print("* * * *")

# step2    make row with 1 star and 1 print
print("* ", end="")
print("* ", end="")
print("* ", end="")
print("* ", end="")

# step3   use loop coz we using same steps multiple times

for j in range(4):
    print("* ", end="")

# step4   layman - use loop coz we using same steps multiple times

for j in range(4):
    print("* ", end="")
print()
for j in range(4):
    print("* ", end="")
print()
for j in range(4):
    print("* ", end="")
print()
for j in range(4):
    print("* ", end="")
print()

# step5   again we r using multiple statements

for i in range(4):
    for j in range(4):
        print("* ", end="")
    print()

# step5

for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()
