'''
This file is meant to test the DiffWord class
'''

from DiffWord import DiffWord

if __name__ == "__main__":
    test = DiffWord()
    print test
    print test.getIndex()

    test2 = DiffWord("Hello", True, [1,1])
    print test2
    print test2.getWord()
    print test2.getIndex()
    print test2.isDiff()
    print test2.get_pos_in_original()
    print test2.get_pos_in_derived()
