def reverse(string):
	word=" "
	
	for i in string:
		word = i+ word 
	return word
string= input('enter the word:')

print("The reversed word is",reverse(string))