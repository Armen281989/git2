
      # 1
# dict1 = {'name': 'Armen', 'age': 30, 'months': 'hulis', 'dey': 2}
# print(dict1)

     # 2
# dict1 = {'name': 'Armen', 'age': 30, 'months': 'hulis', 'dey': 2}
# dict1['avto'] = 'bmw'
# print(dict1)

     # 3
# dict1 = {'name': 'Armen', 'age': 30, 'months': 'hulis', 'dey': 2}
# if 'name' in dict1:
# 	print('name ka aystex')
# else:
# 	print('chka ayd anvanum')
#     #  kam
# for i in dict1.keys():
# 	if i == 'name':
# 		print('we have name')
# 	print(i)

   # 4
# dict1 = {'name': 'Armen', 'age': 30, 'months': 'hulis', 'dey': 2}
# dict2 = {'name2': 'Vazgen', 'age2': 20, 'months2': 'ogostos', 'dey2': 14}
# dict_list1 = []
# dict_list2 = []
# for i in dict1.items():
# 	dict_list1.append(i)
# for j in dict2.items():
# 	dict_list2.append(j)
# print(dict_list1,dict_list2)


   # 5
# dict1 = {'name': 'Armen', 'age': 30, 'months': 'hulis', 'dey': 2}
# dict2 = dict1.copy()
# print(dict1,dict2)

   # 6
dict1 = {'tiv1': 25, 'tiv2': 54, 'tiv3': 24, 'tiv4': 11, 'tiv5': 87}
for key, value in sorted(dict1.items(), key=lambda item: item[1]):
    print( values)