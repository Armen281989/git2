# import math

# c = float(input('cer jermastijan vorqan e '))
# a = c * math.pi
# if a >= 120 and a <= 128:
# 	print(a, 'You have coronavirus because your result is 120  and it is between 120 to 128')
# elif a < 120:
# 	print(a,'duq chuneq')




# tartiv = {'a': 1, 'j': 1, 's': 1,'b': 2,'k': 2,'t': 2,'c': 3,'l': 3,'u': 3,'d': 4,'m': 4,'v': 4,'e': 5,'n': 5,'w': 5,'f':6 ,'o': 6,'x': 6,'g': 7,'p': 7,'y': 7,'h': 8,'q':8,'z': 8,'i': 9,'r': 9}
# anun = input('greq anun ')
# conv = 0
# for i in anun:
# 	conv += tartiv[i]

# res = math.sqrt(conv)

# if math.ceil(res) < 5:
# 	print(conv, 'yes')
# else:
# 	print(conv, 'no')




import random

convuser = 0
convcomp = 0

user = input('@ntreq ays bareric "avada kedavra, crucio, imperio" ')
user1 = input('@ntreq ays bareric "avada kedavra, crucio, imperio" ')
user2 = input('@ntreq ays bareric "avada kedavra, crucio, imperio" ')

user = user.upper()
user1 = user1.upper()
user2 = user2.upper()

comp = ['avada kedavra',  'crucio', 'imperio']
a = random.choice(comp)
b = random.choice(comp)
c = random.choice(comp)

a = a.upper()
b = b.upper()
c = c.upper()

if user == a:
	convuser += 1

elif user != a:
	convcomp += 1
	convuser -= 1

if user1 == b:
	convuser += 1

elif user != b:
	convcomp += 1
	convuser -= 1

if user2 == c:
	convuser += 1

elif user != c:
	convcomp += 1
	convuser -= 1

else:
	print('greq jisht barer')



print('cer @ntrutyunner ','1-',user, '2-',user1, '3-',user2)
print('komp @ntrutyun ','1-',a,'2-',b,'3-',c)
print('')
print(' cer hashiv ',convuser,'\n comp hashiv ',convcomp)