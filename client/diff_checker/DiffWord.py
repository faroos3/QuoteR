'''
This is going the be the different word class used to help evaluate which words are different, and which are not.
'''

class DiffWord:

    #honestly, isDifferent should always be True


    def __init__(self, OWord = "", isDiff = True, idex = 1000000000):
        #default constructor for a word for some reason.
        self.word = OWord #what the word is
        self.isDifferent = isDiff #if the word is different or nah
        self.index = idex #some arbitrary large number.

    def __str__(self):
        return self.word

    #Observers
    def getWord(self): #get the word
        ans = self.word
        return ans

    def isDiff(self):
        return True == self.isDifferent

    def getIndex(self):
        return self.index
