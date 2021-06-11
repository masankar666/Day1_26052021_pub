'''
June 10 
Task2: Sets

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2
'''
#Create two empty sets
print('--Using set empty method ')
empty_a = set()
empty_b = set()
print (empty_a)
print (empty_b)
print(type(empty_a))
print(type(empty_b))

print('--Using set update method ')

#update set1 with 7,8,9,1,2,3,4,5,0
y = {7,8,9,1,2,3,4,5,0}
empty_a.update(y)

#update set2 with 4,5,6,0
z = {4,5,6,0}
empty_b.update(z)

print (empty_a)
print (empty_b)
print(type(empty_a))
print(type(empty_b))


#check whether set2 is subset of set1 or no ?
print('--Using set subset method ')
subset_a = {7,8,9,1,2,3,4,5,0}
subset_b = {4,5,6,0}
subset_c = {1,2,3,4}
subset_d = subset_b.issubset(subset_a)# It is not a subset
subset_e = subset_c.issubset(subset_a)# is a subset
print(subset_d)
print(subset_e)

#check whether both have common elements are no ? 
print('--Using set intersection method ')
intersec1 = {1,2,3,4}
intersec2 = {5,6,7,1,2}
intersec3 = intersec1.intersection(intersec2)
print(intersec1)
print(intersec2)
print(intersec3)

#remove 8 from set 1 and set 2 ==> find the inferences
print('--Using set remove method ')
set_a = {7,8,9,1,2,3,4,5,0}
set_b = {4,5,6,8,0}

set_a.remove(8)
print (set_a)
set_b.remove(8)
print(set_b)


#discard 0 from set 1 and set 2 
print('--Using set discard method ')
set_x = {7,8,9,1,2,3,4,5,0}
set_y = {4,5,6,8,0}

set_x.discard(0)
print (set_x)

set_y.discard(8)
print (set_y)


#find collection of both sets ===> set1 and set2
print('Using set union method ')
union_el = {7,8,9,1,2,3,4,5,0}
union_e2 = {4,5,6,8,0}

c = union_el.union(union_e2)
print (c)

