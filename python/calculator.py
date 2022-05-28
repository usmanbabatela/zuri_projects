'''A calculator that can perform: addition, subtraction, division, multiplication and modulus operations.
It should accept user input
Accepting input from a user'''
from ast import Return
#Welcome Message
def welcome():
    print ("Welcome to AUM calculator")
welcome()
#Select operation to perform
def main_function():
    operation = int (input ('''\nPress the number corresponding to the operation you intend to perform: 
    \t1: Addition
    \t2: Subtraction
    \t3: Division
    \t4: Multiplication
    \t5. Modulus
    \n '''))
    #check if the right option is entered (within the range of allowed options)
    if operation in range(1,6):
        x= input('\n' "Enter the first number: ")
        y= input("Enter the second number: ")
#convert the inputted strings to int
        a,b = int(x),int(y)
    else:
        print('\n' "This is an invalid selection, please select a valid option")
        main_function()
        #Project: Find a way to make the program to exit after entering the wrong option morethan 5 X
#Function definitions
#addition function
    def add (a,b):
        return a + b
#subtraction function
    def subtract (a,b):
        return a-b
#division function
    def divide (a,b):
        return a/b
#multiplication function
    def multiply (a,b):
        return a*b
#modulus function
    def modulus (a,b):
        return a%b
#Conditional Statements
    if operation == 1:
        print ('\n' '{} + {} = '.format(a,b), add(a,b))
    elif operation == 2:
        print ('\n''{} - {} = '.format(a,b), subtract(a,b))
    elif operation == 3:
        print ('\n''{} / {} = '.format(a,b), divide(a,b))
    elif operation == 4:
        print ('\n''{} * {} = '.format(a,b), multiply(a,b))
    elif operation == 5:
        print ('\n''{} modulo {} = '.format(a,b), modulus(a,b))
    else:
        print ('\n' "This is an invalid selection")
    repeat()
#Define another function to accommodate repeating the process
def repeat():
    choice = (input ('''\nWould you like to perform another operation? 
    \tPress 'Y' for Yes and 'N' for No : 
    \n '''))
    if choice.upper()=='Y':
        main_function()
    elif choice.upper()=='N':
        print ("Thanks for enjoying the calculator!!!")
        input("press enter to exit")
    else:
        input("press enter to exit")
#Call main_function() outside of the function to ensure that the function runs.
main_function()





#There are opportunities to introduce more error-handling throughout the program. 
# For starters, you can ensure that the program continues to run even if the user types plankton when asked for a number. 
# As the program is right now, if number_1 and number_2 are not integers, the user will get an error and the program will stop running. 
# Also, for cases when the user selects the division operator (/) and types in 0 for their second number (number_2), the user will receive a ZeroDivisionError: division by zero error. 
# For this, you may want to use exception handling with the try ... except statement. Additionally, you may want to rewrite part of the program with a loop statement.
# There are many ways to handle errors and modify and improve each and every coding project. It is important to keep in mind that there is no single correct way to solve a problem that we are presented with.