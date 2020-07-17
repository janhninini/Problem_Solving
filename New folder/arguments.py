'''
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello','hi','bye','bye')        
'''

import sys
print("enter your fav book")
first_book= sys.argv[1]
first_author= sys.argv[2]

second_book= sys.argv[3]
second_author= sys.argv[4]

print("your most fav book is"+first_book)
print("author of most fav book is"+first_author)

print("your next fav book is"+second_book)
print("author of nxt fav book is"+second_author)
