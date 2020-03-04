print('greq 0-10 zuyg tver ')
zuyg = int(input('0-10zuyg tiv ')) 

print(zuyg == 2 or zuyg == 4 or zuyg == 6 or zuyg == 8 or zuyg ==10)




# import time
# print(8)
# plis = input('plis write -  ') == '-'
# print(3)
# time.sleep(2)
# print('8-3=5',plis, '\n thanks',)

# print(8)
# plis1 = input('plis write +  ') == '+'
# print(3)
# time.sleep(2)
# print('8+3=11',plis1,'\n very good')

# print(8)
# plis2 = input('plis write *  ') == '*'
# print(3)
# time.sleep(2)
# print('8*3=24',plis2,'\n thanks')

# print(8)
# plis3 = input('plis write /  ') == '/'
# print(3)
# time.sleep(2)
# print('8/3=2,66666667',plis3,'\n very good')



def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y
 
num1 = float(input("Enter first number: "))
choice = input("Enter choice(+/-/*//): ")
num2 = float(input("Enter second number: "))

if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input:")