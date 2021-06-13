
Dict = dict({1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]})
print("\nDictionary with the use of dict(): ")
print(Dict)

print("#bio-botany")
print(Dict[3][0])

print("##botany")
print(Dict[3][0][4:])

print("###bobtn")
print(Dict[3][0][0::2])

print("####zoo")
print(Dict[3][1][4:7])

print ('#######----------########')
dict1 = {1:["english","maths","science",["history", "civics", "Geo-graphy",(45,46,47)]], 2:[10,[[20,[99]]],30], 3:("bio-botany","bio-zoology","Algebra")}
#graphy
print(dict1[1][3][2][4:])

#46

print(dict1[1][3][3][1])
#99
print(dict1[2][1][0][1][0])
#20
print(dict1[2][1][0][0])
#botany
print(dict1[3][0][4:])
print ('#######----------########')




print ('#######----------########')
myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}


print(myfamily)

print(type(myfamily))


print('name of child3')
print(myfamily["child3"]["name"])
print('year of child2')
print(myfamily["child2"]["year"])
print ('#########################')



print ('#######----------########')
Task= {"name": "John","age": 30,"married": True,"divorced": False,"children": ("Ann","Billy"),"pets": None,"cars": [{"model1": "BMW 230", "mpg1": 27.5},{"model2": "Ford Edge", "mpg2": 24.1}]}

print ('print Billy ?')
print(Task["children"][1])

print ('print model2 name?')
print(Task["cars"][1]["model2"])

print ('print model1 mpg1?')
print(Task["cars"][0]["mpg1"])

print ('print divorced status?')
print(Task["divorced"])

print ('print age?')
print(Task["age"])

print ('print 230?')
print(Task["cars"][0]["model1"][4:])

print ('print 7.5?')
S = str(Task["cars"][0]["mpg1"])
print(S[1:])

