import json

# num = [1,3,5,7,98, 'name']

# file_name = 'num.json'
# with open (file_name, 'w') as f:
# 	json.dump(num,f)


name = input('cer anun#? ')
password = input('greq cer gaxtnabar@ ')
age = int(input('cer tariq? '))
login = input('cer login greq ')


player_1 = {'name':name,'age': age, 'password': password, 'login': login, 'point':[12,36,54],}
player_2 = {'name':'armen','age':30}
player_3 = {'name':'artur','age':30}





mylist = []
mylist.append(player_1)

file_name = 'nume.json'

with open (file_name, 'w') as f:
	json.dump(mylist,f)

with open (file_name,) as fl:
	result = json.load(fl)

	for i in result:

		print(i['name'])
		print(i['age'])
		print(i['name'], 'cer gaxtnabar', i['password'], 'isk tariq@ ', i['age'], 'point#', i['point'])
		print('point- ',i['point'][0] + i['point'][1] + i['point'][2])
		print(sum(i['point']))