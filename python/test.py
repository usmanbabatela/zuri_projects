'''def welcome():
    print("sannu")
welcome()
x = int(input ("enter a number: "))
count = 0
for x in range(1,6):
    if count <=5:
        count+=1
        print("ok" + str (count))
        welcome()
    else: 
        print('\n' "This is an invalid selection, please select a valid option")'''

def welcome():
    print("sannu")
welcome()
def sannu():
    operation = int(input ("operation is: "))
    count = 1
    if operation in range(1,6):
        x= input('\n' "Enter the first number: ")
        y= input("Enter the second number: ")
#convert the inputted strings to int
        a,b = int(x),int(y)
        print (a+b)
    else:
        print('\n' "This is an invalid selection, please select a valid option")
        count += 1
        print (count)
    while count < 5:
        sannu()
    else:
        print("press enter to exit")
sannu()
