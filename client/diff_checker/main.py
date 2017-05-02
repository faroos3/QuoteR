'''
This is going to be where Samad test things out with text files or whatever.
Going to see if I can split up files line by line,
put them into a list, use a data
structure, all that jazz.
'''

from DiffWord import DiffWord

# function to get the words in a file in a nice interface
# f should be an open file


def get_words(f):
    word_list = []  # where the words will go
    for line in f:
        # need to clean up the words a bit
        line_list = line.split()
        # print "line_list is:", line_list
        for word in line_list:
            word = word.replace(
                '.',
                '').replace(
                ',',
                '').replace(
                '!',
                '').replace(
                '?',
                '')
            word_list.append(word.lower())
        # now split the line
        # for word in line_list:
            # word_list.append(word)
    return word_list


'''
This is the helper function that will be called if the lengths of both
entries are the same. Returns a list of DiffWords
'''


def same_length_list(words1, words2):
    a_list = []
    for i in range(len(words1)):
        if(words1[i] == words2[i]):
            word = DiffWord(words1[i], False, [i, i])
            # print "This should be the same:", word.getIndex(), "And isDiff
            # returns:", word.isDiff()
            a_list.append(word)
        else:
            diff_word1 = DiffWord(words1[i], True, [i, -1])
            diff_word2 = DiffWord(words2[i], True, [-1, i])
            a_list.append(diff_word1)
            a_list.append(diff_word2)
    return a_list


'''
This is the helper func that'll be called if the words are of different
lengths. will return strings of diff length.
'''
'''
words2 is the longer list
'''

def diff_length_list(words2, words1):
    a_list = []
    offset = 0
    for i in range(len(words1)):
        if(words1[i] == words2[i + offset]):
            word = DiffWord(words1[i], False, [i, i])
            # print "This should be the same:", word.getIndex(), "And isDiff
            # returns:", word.isDiff()
            a_list.append(word)
        else:
            if(words1[i] == words2[i + offset + 1]):
                #checks next work in line
                diff_word2 = DiffWord(
                    words2[i + offset], True, [-1, i + offset])
                nextword = DiffWord(words1[i], False, [i, i + offset + 1])
                offset += 1
                #changes offset to not look at same words twice
                a_list.append(diff_word2)
                a_list.append(nextword)
            elif(words1[i + 1] == words2[i + offset]):
                diff_word1 = DiffWord(words1[i], True, [i, -1])
                a_list.append(diff_word1)

            else:
                diff_word1 = DiffWord(words1[i], True, [i, -1])
                diff_word2 = DiffWord(words2[i], True, [-1, i])
                a_list.append(diff_word1)
                a_list.append(diff_word2)
    return a_list


'''
This function will create a list of DiffWords between the two lines of text.
'''


def get_DiffWords(words1, words2):
    ans_list = []
    # Assuming words1 and words2 aren't of equal length,
    # Basically, what this will have to do, is go through the longer
    # description, and then go until it has is different, it will
    # check until it is the same again, and will keep going.
    # ans_list will be a list of DiffWords with their
    # Different value being if the word is different from its
    # index in the original or no. Like it says in the DiffWord
    # file, the first index in the tuple of .getIndex is the
    # locaiton of the word in the original, and the location
    # of it in the derived is the second. A value of -1 means
    # it does not even show up in that place.

    num_words1 = len(words1)
    num_words2 = len(words2)

    more_words = max(num_words1, num_words2)
    less_words = min(num_words1, num_words2)
    same_length = num_words1 == num_words2  # use to see which helper to call
    if(same_length):
        ans_list = same_length_list(words1, words2)
    else:
        if(num_words1 > num_words2):
            ans_list = diff_length_list(words1, words2)
        else:
            ans_list = diff_length_list(words2, words1)

    # #get the words from there
    # i = 0 #going to keep track of the index as well
    # for index in range(less_words):
    #     i = index #to help keep track.
    #     #so this works until you get to a spot where there is a
    #     #diff number of words (i.e. instead of "killing"
    #     #"there's "bad code". It then assumes everything
    #     #is different. So, in order to fix this,
    #     #I'll try getting to until a word is different,
    #     #break, save the index, keep going until
    #     #the words start up to be the same again
    #     #and repeat. While the words ain't
    #     #the same, it'll keep making
    #     #diff words. Maybe I can split
    #     #that up into functions.
    #     if(words1[index] == words2[index]):
    #         #if the words are the same, have a
    #         #DiffWord with isDiff = False
    #         word = DiffWord(words1[index], False, [index, index])
    #         print "This should be the same:", word.getIndex(),
    #         "And isDiff returns:", word.isDiff()
    #         ans_list.append(word)
    #     if(words1[index] != words2[index]):
    #         break
    #         # word1 = DiffWord(words1[index], True, [index, -1])
    #         # word2 = DiffWord(words2[index], True, [-1, index])
    #         # print "Word1's indices are:", word1.getIndex(),
    #           "And isDiff returns:", word1.isDiff()
    #         # print "Word2's indices are:", word2.getIndex(),\
    #           "And isDiff returns:", word2.isDiff()
    #         # ans_list.append(word1)
    #         # ans_list.append(word2)

    return ans_list


if __name__ == "__main__":
    f1 = open("tragedy_test.txt")  # your original text
    f2 = open("test_tragedy_bad.txt")  # what the Google Voice APi will get
    # get the words in each file
    f1_words = get_words(f1)
    f2_words = get_words(f2)

    # get the number of words of each list
    num_f1_words = len(f1_words)
    num_f2_words = len(f2_words)

    # The following is for testing purposes.
    print "There are ", num_f1_words, "in the original file."
    print "There are ", num_f2_words, " in the file derived from voice."
    print "The words in f1 (original):\n"
    for word in f1_words:
        print word,

    print "\n\nThe words in f2 (derived):\n"
    for word in f2_words:
        print word,
    # end testing purposes. the only differences between
    # the two tests are the names changed to Moorthy, the student
    # writing bad code (instead of the master
    # dying), the change on one word
    # to badDocumentation, and bad code at the end.
    print "\n\n"
    # see if the DiffWord worked

    diffWords = get_DiffWords(f1_words, f2_words)
    for word in diffWords:
        if(word.isDiff()):
            print str(word) + " is different."
        else:
            print str(word) + " is not different."
