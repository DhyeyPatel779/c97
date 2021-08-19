name = input('Enter your introduction')
print(name)
wordCount = 1
characterCount = 0
for wcount in name:
    characterCount=characterCount+1
    if (wcount==' '):
        wordCount=wordCount+1 

print('Number of characters in the string')
print(characterCount)    

print('Number of words in the string')
print(wordCount)