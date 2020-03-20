# listt = [4,5,21,65,87,64]
# x = 0
# for i in listt:
# 	x += i / 2
# print(x)


# listt = [12,35,21,87,65]
# x = listt[0]
# for i in listt:
# 	if i > x:
# 		x = i
# print(x)



# listt = [54,69,24,31,14]
# x = 0
# for i in listt:
# 	x += i
# x /= len(listt)
# print(x)


# listt1 = [40,5,21,65,87,64]
# lisst2 = [44,51,23,67,4,69]
# for i in listt1:
# 	for j in lisst2:
# 		if i % j == 0:
# 			print(i)



# listt1 = [40,5,21,65,87,64]
# lisst2 = [44,51,23,67,4,69]
# x = 21
# if x in listt1:
# 	print('21 listt1 e ')
# if x in lisst2:
# 	print('21 listt2 e ')




import random
mast = ['sirt ','xar ','xach ','qyap ']
qar = ['9','10','j','q','k','t']
kalod = []
for i in mast:
	for j in qar:
		result = i + j
		kalod.append(result)
random.shuffle(kalod)
print(kalod)
Armen = []
Artur = []
for i in range(5):
	x = kalod.pop()
	Armen.append(x)
	y = kalod.pop()
	Artur.append(y)
trump = kalod.pop()

Armen.sort()
Artur.sort()

print('   Armen',Armen)
print('')
print('   Artur',Artur)
print('')
print('   trump',trump)
print('')

choise = input('vercnum es xaxaqar Armen? ') == 'y'
if choise:
	Armen.append(trump)
	for i in range(2):
		x = kalod.pop()
		Armen.append(x)
	for i in range(3):
		y = kalod.pop()
		Artur.append(y)

else:
	choise2 = input('Artur vercnum es xaxaqar@? ')
	if choise2:
		Artur.append(trump)
		for i in range(2):
			x = kalod.pop()
			Artur.append(x)
		for i in range(3):
			y = kalod.pop()
			Armen.append(y)

Armen.sort()
Artur.sort()

print('Armen',Armen)
print('')
print('Artur',Artur)
print('')

	

