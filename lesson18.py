# set1 = {12,23,'11','hello'}
# print(set1)



# thisset = {'apple','banaa', 'cherry'}
# for x in thisset:
# 	print(x)


# thisset = {'apple', 'banana', 'cherry'}
# print('banana' in thisset)

 # avelacnum e myusi mej
# set1 = {'a', 'b', 'c'}
# set2 = {1,2,3, 'a'}

# set3 = set1.union(set2)
# print(set3)


# Set, Frozenset
# set1 = {12,14,11, 'hello'}
# set2 = {14,3,141, 'world'}
# set3 = {11,3,145, 'mery'}
# list1 = [221,21,34,67,12,21,34]

# frozenset   chi avelacnum vochmi ban
# fr_set = frozenset({12,25,35,64})
# fr_set.add('l')
# print(fr_set)


# list
# c = set(list1)
# print(c)
# list1 = list(c)
# print(list1)


# for
# new_set = {i ** 2 for i in range(10)}
# print(new_set)


# add
# set1.add(123)
# print(set1)

# clear
# print(type(set2))
# set2.clear()
# print(set2)


# copy
# new_set = set1.copy()
# print(new_set)


# difference cuyc e talis tarberutyun@
# print(set1.difference(set2,set3))


# difference_update jnjum e vor krknvum e
# set1.difference_update(set2)
# print(set1)

# discard jnjum e element
# set1.discard(17)
# set1.remove(17)
# print(set1)


#  intersection krknvox berum e
# print(set1.intersection(set2))

# isdisjoint berum e tru ete krknvox chka
# print(set1.isdisjoint(set2))


# issubset berum e true ete ka erku setum nuyn baner
# print(set1.issubset(set2))


# pop verjic vercnum e
# x = set1.pop()
# print(x)


# symmetric_difference
# x = {'apple', 'banan', 'cherry'}
# y = {'google', 'microsoft', 'apple'}
# z = x.symmetric_difference(y)
# print(z)


# union  hanum e krknvox
# x = {'apple', 'banan', 'cherry'}
# y = {'google', 'microsoft', 'apple'}
# z = x.union(y)
# print(z)
 


# update
# set1.update(set3)
# print(set1)


# xndir xanutic gnum katarelis gin talis
# from math import floor
# guyn = int(input('qani guyn eq uzum? '))
# cost = floor(((40 + guyn * 5)/ 10) * 11)
# print(cost)


# xndir eranish tiv bajanvum e te voch  "gapful"
gapful1 = input('grel eranish tiv ')
num = gapful1[0] + gapful1[2]
if int(gapful1) % int(num) == 0:
	print('tiv@ gapf ')

else:
	print('tiv gapf che, sxal')

