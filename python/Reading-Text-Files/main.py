# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgi import print_arguments
import string
#print (string.punctuation)

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt','r') as f:
        content=f.read()
        return content

def count_words():
    # [assignment] Add your code here
    text = read_file_content("story.txt")
    #convert text to lower case
    x = text.lower()
    #remove punctuations
    y = x.translate(str.maketrans('', '', string.punctuation))
    words = y.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count [word] = 1
    print (word_count)        
count_words()
