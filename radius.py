''''
Tasks May 27:

pgm1:

    radius = 20 
    calculate perimeter of circle : 2 pi radius
'''
r = float(20)  # radius will be 20.0
radius = r
pi = 3.14
peri = 2 * pi * radius
print("pgm1:")
print("radius = ",r)
print ("calculate perimeter of circle = ",peri)

''''
Tasks May 27:

pgm2: 
    
    radius = 99.10  height = 10.5
    area of cone = 1/3 pi r2 h
    output ===> int 
'''
print("pgm 2:")
r = float(99.10)  # radius will be 99.10
h = float(10.5)   # height will be 10.5
radius = r
height = h
pi = 3.14
area = 1/3 * pi * (r * r) * h
#area = (int(area))

peri = 2 * pi * radius
print("radius = ",r)
print ("area of cone  = ",(int(area)))
print ("calculate perimeter of circle = ",(int(peri)))


'''
pgm3: 
    
    five datatypes: 10-15 line program
        #str int float boolen complex
'''
#Built-in Data Types
#string -> Text Type:	str
z = "Data Types"
print(type(z))

#str 2
y = 'Data Types'
print(y)
print(type(y))

#Numeric Types:	int, float, complex
#integer
x = 5
print(x)
print(type(x))

#float
flo = 5.8998
print(flo)
print(type(flo))

#complex
x = 1j
print(x)
print(type(x)) 

#Boolean Type:	bool
t = True
f = False
print(t)
print(f)
print(type(t))
print(type(f))

'''
pgm4: 
    
    rules for creating variable
'''

print("Must be start with underscore and it can't start with numeric")
print("using alpha numeric possibly.but numeric alpha as it not possible. ")
print(" start with underscore but can't start with operator")
print(" A (capital )or a(small letter) treat as difference (case sensitive)")

#Legal variable names: (Valid syntax)
a = 10
b = 2.5
_n = '5'
t_f = "TV"
m34 = 20
myvar = "Sankar"
my_var = "Sankar"
_my_var = "Sankar"
myVar = "Sankar"
MYVAR = "Sankar"
myvar2 = "Sankar"

print (a)
print (b)
print (_n)
print (t_f)
print (m34)
print (myvar)
print (my_var)
print (_my_var)
print (myVar)
print (MYVAR)
print (myvar2)
'''
#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
print (2myvar)
print (my-var)
print (my var)

'''
