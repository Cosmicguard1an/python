name=input('Enter your name?')
print(name)
characterNum = 0
wordNum=1
for i in name:
    if(i==' '):
        wordNum = wordNum + 1
    characterNum = characterNum + 1
print('There are ' + str(characterNum) + ' characters in your name. Also, there is ' + str(wordNum) + ' words in your name.')

