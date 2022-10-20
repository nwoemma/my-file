name_age = [('emma',18), ('wisdom',19), ('uche', 20), ('clara',26)]
print('names of students and their age')
print(name_age)
name_age.sort(key = lambda x:x[1])
print('\n sorting the list of tuples: ')
print(name_age)