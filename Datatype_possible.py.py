'''
Tasks May 28, 2021

#Task1:
#       int   str   bool  float
#int 
#str
#bool
#float
'''
#Answer as possible table conversion
"""
#TYPE conversion possible table
	INT	FLOAT	BOOL	STR
INT	X	YES	YES	YES
FLOAT	YES	X	YES	YES
BOOL	YES	YES	X	YES
STR	NO	NO	YES	X

String to int not possile
String to float not possible
"""
#Task1 Pgm's workouts:
#Int,str declare last stored value got
a = 100
a = "54"
print(a)
print(int(a))
print(type(a))

#str to int convert
a = "1100"
a = int(a)
print(a)
print(int(a))
print(type(a))

#Int to float conversation

x = 4454
y = float(x)
print (x)
print (type(x))
print (y)
print (type(y))

#Int to bool conversation

num = int(5665)
boolofnum = bool(num)
print (num)
print (type(num))
print (boolofnum)
print (type(boolofnum))

#Int to str conversation

A = 10
B = str(A)
print (A)
print (type(A))
print (B)
print (type(B))

#str act as universal
a = "10026"
b = "apple"
print(a)
print(int(a))
print(type(a))

print(b)
print(type(b))
'''
print(b)
print(int(b))
print(type(b))
Traceback (most recent call last):
  File "E:/PDF edited 2019/TY 2019/PERS/shift/python3/my_files/using_input.py", line 68, in <module>
    print(int(b))
ValueError: invalid literal for int() with base 10: 'apple'
'''

#Float convert to int possible

i = 554.55
k = int(i)
print (i)
print (type(i))
print (k)
print (type(k))

#float convert to bool possible

fl = 61562.2656
boo = bool(fl)
print (fl)
print (type(fl))
print (boo)
print (type(boo))

#float convert to str possible

fls = 15151.65454
flstoboo = str(fls)
print (fls)
print (type(fls))
print (flstoboo)
print (type(flstoboo))


#boolean convert to int possible

str = True
str2 = int(str)
print (str)
print (type(str))
print (str2)
print (type(str2))

#boolean convert to float possible

boolean = False
boolean_fl = float(boolean)
print (boolean)
print (boolean))
print (boolean_fl)
print (type(boolean_fl))

#boolean convert to str possible

boolean_str = True
boolean_str2 = str(boolean_str)
print (boolean_str)
print (type(boolean_str))
print (boolean_str2)
print (type(boolean_str2))

# String to int not possile

#str_int = "True"
#str_int2 = int(str_int)
#print (str_int)
#print (type(str_int))
#print (str_int2)
#print (type(str_int2))
'''
o/p:
Traceback (most recent call last):
  File "E:/PDF edited 2019/TY 2019/PERS/shift/python3/my_files/using_input.py", line 229, in <module>
    str_int2 = int(str_int)
ValueError: invalid literal for int() with base 10: 'True'
'''
# String to float not possible

#str1 = "False"
#fl2 = float(str1)
#print (str1)
#print (type(str1))
#print (fl2)
#print (type(fl2))
'''
o/p:
Traceback (most recent call last):
  File "E:/PDF edited 2019/TY 2019/PERS/shift/python3/my_files/using_input.py", line 153, in <module>
    fl2 = float(str1)
ValueError: could not convert string to float: 'False'
'''
#String convert to boolean possible

strboo = "True"
boostr = bool(strboo)
print (strboo)
print (type(strboo))
print (boostr)
print (type(boostr))





