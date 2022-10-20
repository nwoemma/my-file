def letterToNumber(word):
    numkey = []
    tmp = 1
    for i in word:
        tmp = i.lower()
        numkey.append(ord(tmp.lower())-ord('a'))
    return numkey
word = input('enter a letter')
numberkey = letterToNumber(word) 
print(numberkey)