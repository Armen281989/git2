
# # ogtagorcum enq fail
# # f = open('les16.txt', 'r')
# # print(f.read())

#  #  tpum e tarer
# f = open('les16.txt', 'r')
# # print(f.read(5))
# # f.seek(0)  

# #   #  toxern e tpum
# # print(f.read(5))
# # print(f.readline())


#    # ckl e frum
# # print(f.readline())
# # print(f.readline())

# # for i in f:
# # 	print(i)

#   # pakum e fail
# f.close()

  # fail e sarqum 
# file = open('web.txt', 'a')


# file.write('barev bolorin, aysor lav or e; cez hajoxutyun')
# file = open('web.txt', 'r')
# print(file.read())


#   #  jnjum e faili gracner norn e avelacnum
# file = open('web.txt', 'w')

# file.write('barev bolorin, ')
# file = open('web.txt', 'r')
# print(file.read())


  # fail ete ka eror etalis, ete chka nor e sarqum
# file = open('w.txt', 'x')

# file.write('barev bolorin, ')
# file = open('w.txt', 'r')
# print(file.read())

# file.close()

#   # jnjum e fail
# import os
# os.remove("web.txt")

# file = open('w.txt', 'w', encoding = 'utf-8')
# file.write('barev bolorin, կլօր ')
# file = open('w.txt', 'r',)
# print(file.read())

with open('h.txt', 'wt', encoding = 'utf-8') as file:
	possword = input('write your password, բառեվ')
	file.write(possword)
	print(file)