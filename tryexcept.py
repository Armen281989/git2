# try:
# 	print('Hello')
# except NameError:
# 	print("Variable x is not defined")
# except:
# 	print("Something else went wrong")



# try:
# 	print("Hello")
# except:
# 	print("Something went wrong")
# else:
# 	print("Nothing went wrong")


# try:
# 	print(x)
# except:
# 	print("Something went wrong")
# finally:
# 	print(x)


# #The try block will raise an error when trying to write to a read-only file:

# try:
# 	f = open("demofile.txt") # becouse i dont have (w) in my code
# 	f.write("Hello World")
# except:
# 	print("Something went wrong when writing to the file")
# finally:
# 	f.close()

# #The program can continue, without leaving the file object open


# list_1 = ['Ani','Xcho','Vrej','Mane']
# while True:
# 	try:
# 		i = int(input('input number'))
# 		print(list_1[i - 1])
# 		break
# 	except IndexError:
# 		print("input out of index")
# 	except ValueError:	
# 		print("please input number")


# while True:
#     mark = {"Anna" : 10, "Narek" : 9, "Mane" : 7}
#     try:
#         name = input("Name: ")
#         for i in name:
#             if i.isalpha() == False:
#                 raise ValueError
#         print(name,mark[name],'years old')
#         break
#     except KeyError:
#         print(name, "don't found")
#     except ValueError:
#         print("Invalid input")


# while True:

# 	try:
# 		num = int(input())
# 		x = 5/ num
# 	except ZeroDivisionError:	
# 		print('second opprtator could not be 0')
# 	except ValueError:
# 		print('please input number')	
# 	else:
# 		print(x)
# 		break	

# print(a if a > b else b)


# # PYTHON
# a,b = b,a
	






