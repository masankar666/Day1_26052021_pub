'''
#Task2. Get two values (input) ===> number, string

#7 , "python" ===> pythonpythonpythonpythonpythonpythonpython777777

#3 , "perl"   ===> perlperlperl3333
'''

num = int(input("give the number :"))
word = input("give the word :")

le = len(word)
r = (word+' ') * num
p = (num) * le
print(r +(str(num)+' ') * le)
