# 1 Write a Python program to create a set
# et1 = {12,23,25,'thanks','11','hello'}
# print(set1)



#  2  Write a Python program to iteration over sets
# set1 = {12,23,25,'thanks','11','hello'}
# set2 = {14,3,141,12, 'world'}
# print(set1.intersection(set2))


# 3   Write a Python program to add member(s) in a set
# set1 = {12,23,25,'thanks','11','hello'}
# set1.add('s')
# print(set1)


# 4  Write a Python program to remove item(s) from set 
# set1 = {12,23,25,'thanks','11','hello'}
# set1.remove('11')
# print(set1)

# 5  Write a Python program to remove an item from a set if it is present in the set
# set1 = {12,23,25,'thanks','11','hello'}
# set2 = {14,3,141,12, 'world'}
# set1.difference_update(set2)
# print(set1)


# 6  Write a Python program to create an intersection of sets.
# setx = set(["green", "blue"])
# sety = set(["blue", "yellow"])
# setz = setx & sety
# print(setz)


# 7  Write a Python program to create a union of sets
# set1 = {12,23,25,'thanks','11','hello'}
# set2 = {14,3,141,12, 'world'}
# set3 = set1.union(set2)
# print(set3)

# 8  Write a Python program to issubset and issuperset
# set1 = {12,23,25,'thanks','11','hello'}
# set2 = {14,3,141,12, 'world'}
# print(set1.issubset(set2))

# 9  Write a Python program to clear a set
# set1 = {12,23,25,'thanks','11','hello'}
# set1.clear()
# print(set1)

# 10   Write a Python program to find maximum and the minimum value in a set
# sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55]) 
# print(max(sets)) 
# print(min(sets))


# 11  Write a Python program to find the length of a set
# seta = set([5, 10, 3, 15, 2, 20])
# print(len(seta))




   # zuyg tveri 1 tarberak

# print('                           խնդրեմ գրեք պատահական 5 թիվ')
# list0 = int(input('ձեր 1 թիվը '))
# list2 = int(input('ձեր 2 թիվը '))
# list3 = int(input('ձեր 3 թիվը '))
# list4 = int(input('ձեր 4 թիվը '))
# list5 = int(input('ձեր 5 թիվը '))
# zuyg = [] 
# kent = []

# if list0 % 2 == 0:
# 	zuyg.append(list0)
# else:
# 	kent.append(list0)


# if list2 % 2 == 0:
# 	zuyg.append(list2)
# else:
# 	kent.append(list2)


# if list3 % 2 == 0:
# 	zuyg.append(list3)
# else:
# 	kent.append(list3)


# if list4 % 2 == 0:
# 	zuyg.append(list4)
# else:
# 	kent.append(list4)


# if list5 % 2 == 0:
# 	zuyg.append(list5)
# else:
# 	kent.append(list5)

          
# print("Ձեր մութքագրած զույգ թվերը: ", zuyg) 
# print("Ձեր մութքագրած կենտ թվերը: ", kent) 



   # zuyg tveri 2 tarberak

# list1 = [10, 21, 4, 45, 66, 93, 1] 
# list2 = 0
# list3 = 0
# for i in list1: 
      
#     if i % 2 == 0: 
#         list2 += 1

#     else:
#     	list3 += 1
  
# print("zuyg tveri qanak: ", list2) 
# print("kent tveri qanak: ", list3) 


 

  # zuyg tveri 3 tarberak
# list1 = [8, 10, 19, 25, 5, 16, 12] 
   
# zuyg = [num for num in list1 if num % 2 == 0] 
# qanak = len(zuyg) 
   
# print("zuyq tver: ", zuyg) 
# print("@ndhanur zuyq tveri qanak: ", qanak)




print('   ')
print('      @ntereq inch eq patvirum, nachos = 6$, pizza = 6$, cheeseburger = 10$, jur = 4$, kokakola = 5$')

nachos = 6
pizza = 6
cheeseburger = 10
jur = 4
kokakola = 5
menyu = input('inch kcankanaq? ').split(' ')

if menyu in 'nachos pizza cheeseburger kokakola':
	menyu = nachos + pizza + cheeseburger + kokakola
	x = (menyu / 100 * 7) + menyu
	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','cer patver@ kazmec',x,'$')

elif menyu in 'nachos pizza cheeseburger jur':
	menyu = nachos + pizza + cheeseburger + jur
	y = (menyu / 100 * 7) + menyu
	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','jur',jur,'$','cer patver@ kazmec',y,'$')

elif menyu in 'nachos pizza cheeseburger popcorn':
	menyu = nachos + pizza + cheeseburger + kokakola
	z = (menyu / 100 * 7) + menyu
	print('nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','cer patver@ kazmec',z,'$')

else:
	menyu = nachos + pizza + cheeseburger + kokakola
	x = (menyu / 100 * 7) + menyu
	print('Ձեր պատվեր չկա մենյույում \nՁեզ առաջարկում ենք -','nachos',nachos,'$','pizza',pizza,'$','cheeseburger',cheeseburger,'$','kokakola',kokakola,'$','ընդհանուր կազմեց',x,'$')




