'''
This is going the be the different word class
used to help evaluate which words are
different, and which are not.
'''


class DiffWord:

    #  all the words should be DiffWords

    def __init__(self, OWord="", isDiff=True, idex=[-1, -1]):
        #  default constructor for a word for some reason.
        self.word = OWord  # what the word is
        self.isDifferent = isDiff  # if the word is different or nah
        self.index = idex  # the first position
        #  of the list is the position of the
        #  word in the original file, the second position of it is in the
        #  derived file.

    def __str__(self):
        return self.word

    #  Observers
    def getWord(self):  # get the word
        ans = self.word
        return ans

    def isDiff(self):
        return self.isDifferent is True

    def getIndex(self):
        return self.index

    def get_pos_in_original(self):
        return self.index[0]

    def get_pos_in_derived(self):
        return self.index[1]
