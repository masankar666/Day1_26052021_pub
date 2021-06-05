'''
#Task5:

#Get one string (Captial) ==> PYTHON
#Convert middle letter of the string in to small

PYThON
'''
a = input("Give your input: ")

mid_value = len(a) // 2
s = a[:mid_value].upper() + a[mid_value].lower() + a[mid_value+1:].upper()
T = a[:mid_value].lower() + a[mid_value].upper() + a[mid_value+1:].lower()
print(mid_value)
print(s)
print(T)

