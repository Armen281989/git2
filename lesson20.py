# try:
# 	print('helo')
# except:
# 	print('someting wert')
# else:
# 	print('the try except')



# list_1 = ['ani','xcho','vrej','mane']
# while True:
# 	try:
# 		i = int(input('input number'))
# 		print(list_1[i-1])
# 		break
# 	except indexerror:
# 		print('input out index')
# 	except ValueError:
# 		print('please input number')



# # the try block will raise an error when trying to write to a read-only file

# try:
# 	f = open('demofile.txt') # becouse i dont have (w) in my code
# 	f.write('hello word')
# except:
# 	print('something went wrong when file')
# finally:
# 	f.close()



# while True:
# 	mark = {'anna' : 10,'serop': 9, 'mane': 7}
# 	try:
# 		name = input('name: ')
# 		for i in name:
# 			if i.isalpha() == False:
# 				raise ValueError
# 		print(name,mark[name],'years old')
# 		break
# 	except KeyError:
# 		print(name,'dont found')
# 	except ValueError:
# 		print('invalid input')



# while True:
# 	try:
# 		num = int(input())
# 		x = 5 / num

# 	except ZeroDivisionError:
# 		print('second opprtor could not be 0')
# 	except ValueError:
# 		print('please input number')
# 	else:
# 		print(x)
# 		break



# a = 7
# b = 8
# print(a if a > b else b)


# a,b,c = 7,8,9
# print(a,b,c)


# input grac mej prabelnerov e haskanum
# order = input().split(' ')
# print(order)


# print('   ')
# print('      @ntereq inch eq patvirum, nachos = 6$, pizza = 6$, cheeseburger = 10$, jur = 4$, kokakola = 5$')

# nachos = 6
# pizza = 6
# cheeseburger = 10
# jur = 4
# kokakola = 5
# menyu = input('inch kcankanaq? ').split(' ')

# if menyu in 'nachos pizza cheeseburger kokakola':
# 	menyu = nachos + pizza + cheeseburger + kokakola
# 	x = (menyu / 100 * 7) + menyu
# 	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','cer patver@ kazmec',x,'$')

# elif menyu in 'nachos pizza cheeseburger jur':
# 	menyu = nachos + pizza + cheeseburger + jur
# 	y = (menyu / 100 * 7) + menyu
# 	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','jur',jur,'$','cer patver@ kazmec',y,'$')

# elif menyu in 'nachos pizza cheeseburger popcorn':
# 	menyu = nachos + pizza + cheeseburger + kokakola
# 	z = (menyu / 100 * 7) + menyu
# 	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','cer patver@ kazmec',z,'$')

# else:
# 	menyu = nachos + pizza + cheeseburger + kokakola
# 	x = (menyu / 100 * 7) + menyu
# 	print('Ձեր պատվեր չկա մենյույում \nՁեզ առաջարկում ենք -','nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','ընդհանուր կազմեց',x,'$')




order = input().split(' ')

cout = 0
for i in order:
	if i == 'pizza':
		cout += 6
	elif i == 'chesburger':
		cout += 10
	elif i == 'water':
		cout += 4
	else:
		cout += 5
i = cout + cout * 7 / 100
print(i)