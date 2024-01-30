#Task 2: A simple Calculator

#Function for addition(+)
def add(x,y):
    sum = x+y
    return sum

#Function for subtraction(-)
def subtract(x,y):
    sub = x-y
    return sub

#Function for multiplication(x)
def multiply(x,y):
    mul = x*y
    return mul

#Function for division(/)
def divide(x,y):
    div = x/y
    return div

#Function for division(%)
def modulus(x,y):
    div = x%y
    return div

#Taking Inputs
num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
op = (input("Enter the operation you want to perform(+,-,*,/,%):"))

#Calling functions according to user's input values
if op=='+':
    print(num_1,"+",num_2,"=",add(num_1,num_2))
if op=='-':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))
if op=='*':
    print(num_1,"x",num_2,"=",multiply(num_1,num_2))
if op=='/':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
if op=='%':
    print(num_1,"mod",num_2,"=",modulus(num_1,num_2))


