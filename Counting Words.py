intro= input("please enter introduction :")
characterCount=0
wordCount=1
for i in intro:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print ("number of characters :",characterCount)
print ("number of words :",wordCount)