# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# def welcome():
#     print ("Welcome to AUM Anagram Checker! Confirm if two words are Anagrams.")
# welcome()

word = []
anagram = []

def find_anagram(word, anagram):
    word = input('\n' "Enter the first word: ")
    anagram = input("Enter the second word: ")
    if sorted(word)==sorted(anagram):
        return True
    else:
        return False
        welcome()
print(find_anagram(word,anagram))

#To repeat the process
# def repeat():
#     choice = (input ('''\nWould you like to perform another check? 
#     \tPress 'Y' for Yes and 'N' for No : 
#     \n '''))
#     if choice.upper()=='Y':
#         find_anagram(word,anagram)
#     elif choice.upper()=='N':
#         print ("Thanks for using the program!!!")
#         input("press enter to exit")
#     else:
#         input("press enter to exit")
# repeat()
# welcome()







