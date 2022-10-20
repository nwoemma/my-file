def reverse(string):
    word = ""

    for i in string:
        word = i + word
    return word
string = input("enter the word you want reverse: ")
print("the reverse of the word is:",reverse(string))