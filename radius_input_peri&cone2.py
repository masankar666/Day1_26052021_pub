'''
#Task3
    
    radius = 99.10 (float)  height = 10.5 (int)
    area of cone = 1/3 pi r2 h
    output ===> int
'''

#dynamic radius input from user
#r = 99.10
#h = 10
r = float(input("Enter your radius as input:"))
h = int(input("Enter your height:")) 
pi = 3.14
peri = 2 * pi * r
area = 1/3 * pi * (r ** 2) * h
print("Task 2 pgm 1 :")
print("radius = ",r)
print("height = ",h)
print ("calculate perimeter of circle = ",peri)
print ("o/p type integer - calculate perimeter of circle = ",int(peri))
#area of cone
print ("area of cone  = ",(int(area)))

