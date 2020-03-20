# dasaran1 = ['ashot','mariam','armen','artur','ani','valod','mariam','hasmik','arsen','gevor']
# dasaran2 = ['vazgen','gurgen','gayan','artur','ani','valod','mariam','hasmik','arsen','gevor']
# if len(dasaran2) > len(dasaran1):
# 	dasaran2.extend(dasaran1)
# 	print(dasaran2)
# else:
# 	print(dasaran1,'sa 1a dasarani ashakertnern en \n 1b dasaranum ksovoren, ',dasaran2)




print('mutqagreq dprocum grancvac 1 dasarani ashakertneri anunner@')

name_1 = input('greq anunner a dasarani hamar ')
name_2 = input('greq anunner b dasarani hamar ')
araji_a = []
araji_b = []
araji_a.append(name_1)
araji_b.append(name_2)
	
if len(araji_a) == len(araji_b):
	print('araji_a dasranum ksovoren- ',araji_a,'\naraji_b dasaranum ksovoren- ',araji_b)

else:
	print('unennq mi dasaran',araji_a + araji_b)

