# thisdict = {'name':'Aram','year':1994}
# print(thisdict)


# thisdict = {'name':'Aram','age': 1994}
# thisdict['age'] = 2014
# print(thisdict)

# thisdict = {'name':'Aram','year': 1994}
# print(len(thisdict))


#  # avelacnum e dictionary
# thisdict = {'name':'Aram','year':1994}
# thisdict['age'] = 26
# print(thisdict)


#   # diqshn e sarqum
# thisdict = dict(brand='ford',model='mustang',year=1964)
# print(thisdict)



# dict1 = {'name': 'Aram','age': 17}
# dict1.clear()  # jnjum e
# print(dict1)


# dict1 = {'name': 'Aram','age': 17}
# dict1.copy()  #kopia anum
# print(dict1)



# dict1 = {'name': 'Aram','age': 17}
# c = dict1.fromkeys('12345')  #sarqum e nor dict
# print(c)


# dict1 = {'name': 'Aram','age': 17, 'coutry': 'Armenia'}
# print(dict1.get('name')) # tpume valyu


# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())


# for i in dict1.values():
# 	print(i)

# for i in dict1.items():
# 	print(i)

# for i in dict1.keys():
# 	if i == 'name':
# 		print('we have name')
# 	print(i)



# dict1 = {'name': 'Armen','lastname': 'Babayan','taretiv': 1989, 'kendani':'shun','exanak':'garun'}
# print(dict1.keys())
# print(dict1.values())
# dict1['jermastijan'] = 21
# print(dict1)
# del dict1['name']
# print(dict1)



# calod = {'xach':'d','qyap':'k'}
# for i,j in calod.items():
# 	print(i,j, end = ' ,')


calod = {'xach':'d','qyap':'k'}
point = 0
for i in calod.values():
	if i == 'q':
		point += 3
	elif i == 'k':
		point += 4
print('d + k =',point)


