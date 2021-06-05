'''
#capital programs strings

#Task4:

#get two strings from user  computer science  ==> input 

#step 1 ==> comPuter  sciEnce

#step 2 ===> concatenate both ==> comPutersciEnce

#step 3 ===> comPuteRsciEnce
'''

a = input("Give your 1st input: ")
b = input("Give your 2nd input: ")
mid_value_a = len(a) // 2
mid_value_b = len(b) // 2
#s = a[:].upper() + a[mid_value].lower() + a[mid_value+1:].upper()
T1 = a[:mid_value_a].lower() + a[mid_value_a].upper() + a[mid_value_a+1:].lower()
T2 = b[:mid_value_b].lower() + b[mid_value_b].upper() + b[mid_value_b+1:].lower()
print(mid_value_a)
print(mid_value_b)
print(T1)
print(T2)
print(T1 + " " +T2)
print(T1 + T2)

T3 = T1 + T2
mid_value_T3 = len(T3) // 2
T4 = T3[:mid_value_T3].lower() + T3[mid_value_T3].upper() + T3[mid_value_T3+1:].lower()
print(T4)
#T5 = T3[:mid_value_T3].lower() + T3[mid_value_T3].upper() + T3[mid_value_T3+1:].lower()
#print(T5)
