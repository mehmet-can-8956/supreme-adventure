#part1
def division(x,y):
    try:
        return x/y
    
    except ZeroDivisionError:
        
        print("Numbers can not be divided by zero")
        
division(5,0)

#part2
try:
    print(y)
    
except NameError:
    print("It is not defined")

#part3
def value_error(x):
    try:
        return int(x)
    except ValueError:
        print("It is not a number")

a=input("Enter a number please:")
value_error(a)