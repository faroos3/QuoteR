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
        #print "line_list is:", line_list
        for word in line_list:
            word = word.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
            word_list.append(word.lower())
        #now split the line
        #for word in line_list:
            #word_list.append(word)
    return word_list


'''
This function will create a list of DiffWords between the two lines of text. 
'''
def get_DiffWords(words1, words2):
    ans_list = []
    #Assuming words1 and words2 aren't of equal length,
    #Basically, what this will have to do, is go through the longer
    #description, and then go until it has is different, it will
    #check until it is the same again, and will keep going.
    #ans_list will be a list of DiffWords with their
    #Different value being if the word is different from its
    #index in the original or no. Like it says in the DiffWord
    #file, the first index in the tuple of .getIndex is the
    #locaiton of the word in the original, and the location
    #of it in the derived is the second. A value of -1 means
    #it does not even show up in that place. 
    
    return ans_list


if __name__ == "__main__":
    f1 = open("tragedy_test.txt") #your original text 
    f2 = open("test_tragedy_bad.txt")#what the Google Voice APi will get
    #get the words in each file 
    f1_words = get_words(f1)
    f2_words = get_words(f2)

    #get the number of words of each list
    num_f1_words = len(f1_words)
    num_f2_words = len(f2_words)

    
    #The following is for testing purposes. 
    print "There are ", num_f1_words, "in the original file."
    print "There are ",num_f2_words," in the file derived from voice."
    print "The words in f1 (original):\n"
    for word in f1_words:
        print word,

    print "\n\nThe words in f2 (derived):\n"
    for word in f2_words:
        print word,
    #end testing purposes. the only differences between the two tests are the names changed to Moorthy, the student
    #writing bad code (instead of the master dying), the change on one word to badDocumentation, and bad code at the end.

    
