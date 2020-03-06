age = input('erb eq cnvel? ')
if age.isidentifier():
	print('error, grel miayn tiv')
else:
	pass
name = input('cer anun@ ')
if name.isdecimal():
	print('error, grel miayn tar ')
else:
	pass
surename = input(name+ ' ' +'greq cer azganun@ ')
if surename.isdecimal():
	print('eror, grel miayn tar')
else:
	pass
mail = input('greq cer email ')
if '@' not in mail:
	print('error',name,'greq jisht email')
else:
	pass
password = input('mutqagreq gatnabar 8 ic voch pakas, mecatar ev poqratarerov ')
if len(password) >= 8 and len(password) <= 12:
	if password == '[a:z]' and password == '[A:Z]':
		print('ok')
else:
 	print('error')