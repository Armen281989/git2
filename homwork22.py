
   # 1
# def car():


# 	dict1 = {'tiv1': 25, 'tiv2': 54, 'tiv3': 24, 'tiv4': 11, 'tiv5': 87}
# 	for key, value in sorted(dict1.items(), key=lambda item: item[1]):
# 	    print( value)



# car()




# def max(a,b,c):
# 	if a>b and a>c:
# 		print ("maximum is :",a)
# 	elif b>a and b>c:
# 		print ("maximum is :",b)
# 	else:
# 		print ("maximum is :",c) 

# max(max(4,8,2,))




# def maxmin():

# 	number1 = int(input('Enter First number : '))
# 	number2 = int(input('Enter Second number : '))
# 	number3 = int(input('Enter Third number : '))
# 	lst = [number1, number2, number3]
# 	print("The largest of the 3 numbers is : ", max(lst))
# 	print("The smallest of the 3 numbers is : ", min(lst))


# maxmin()


   # 2. Write a Python function to sum all the numbers in a list. 
# def gumarum(a,b,c,d,e):

# 	print(a + b + c + d + e)

# gumarum(8, 2, 3, 0, 7)




    # 3 Write a Python function to multiply all the numbers in a list. 

# def bazmapatkum(a,b,c,d,e):

# 	print(a * b * c * d * e)

# bazmapatkum(8, 2, 3, -1, 7)


    # 4 Write a Python program to reverse a string. 

# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))




  # 5 Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))


  # 6Write a Python function to check whether a number is in a given range.
# def test_range(n):
#     if n in range(10,20):
#         print( "Number %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(15)


  

  # 7  . Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brow Fox')




   # 8   Write a Python function that takes a list and returns a new list with unique elements of the first list. 

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5]))
