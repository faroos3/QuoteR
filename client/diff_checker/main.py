'''
This is going to be where Samad test things out with text files or whatever.
Going to see if I can split up files line by line, put them into a list, use a data
structure, all that jazz.

'''

from DiffWord import DiffWord

#function to get the words in a file in a nice interface
#f should be an open file
def get_words(f):
    word_list = [] #where the words will go
    for line in f:
        #need to clean up the words a bit
        line_list = line.split()
        print "line_list is:", line_list
        for word in line_list:
            word = word.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
            word_list.append(word.lower())
        #now split the line
        #for word in line_list:
            #word_list.append(word)
    return word_list


if __name__ == "__main__":
    f1 = open("tragedy_test.txt") #your original text 
    f2 = open("test_tragedy_bad.txt")#what the Google Voice APi will get
    #get the words in each file 
    f1_words = get_words(f1)
    f2_words = get_words(f2)

    print f1_words
    

    

    
