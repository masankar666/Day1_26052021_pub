'''
#Task3. Get two values (input) ===> string, number

#computer_science, 3 ===> mocputer_scieecn

#biology , 2  ===> iboloyg

'''
a= input("Give the string: ")
b = int(input("Give your number : "))
print(a[:b][::-1] + a[b:len(a)-b] + a[len(a)-b:][::-1])
#c = a[:b][::-1]
#d = a[len(a)-b:][::-1]
#print(c)
#print(d)

#print(c + a[b:len(a)-b] + d)


