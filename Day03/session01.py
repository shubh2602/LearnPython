# String

x = "shubham pandey"
print(x)
print(len(x))
print(x[0])
print(x[13])
print(x.capitalize())    #caps first letter
print(x.casefold())

# slicing

y = "learning python from scratch"
print(y[0:4])             #print(y[start,end,step])
print(y[0:10:2])
print(y[0:len(y)])  # print full string
print(y[::-2])            #reverse with 2 gap

list=["apple,orange,mango,grapes"]        #count as 1 item
List = ["apple", "orange", "mango", "grapes"]
print(List[2])
print(List[0:2])          # ['apple', 'orange']
print(List[0:3:2])        # ['apple', 'mango']
print(List[0:len(List)])    # full list print

set={"apple", "apple", "mango"}
list=["apple", "apple", "mango"]
print(set)                  # not print duplicate
print(list)                 # print duplicates as well