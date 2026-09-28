#1)calculator 
A = int(input("Enter the first number:"))
B = int(input("Enter the second number:"))
print("a = addition")
print("b = subtraction")
print("c = division")
print("d = modules")
print("e = multiplication")
print("f = min")
print("g = max")
C = input("Enter the operator : ")
a = A+B
b = A-B
c = A/B
d = A%B
e = A*B
f = min(A,B)
g = max(A,B)
if  C == a:
    print("The addition of the numbers is :" , a)
elif C == b:
    print("The subtraction of the number is :" , b)
elif C == c :
    print("The division of the number is : " , c )
elif C == d:
    print("The modulues of the number is :" , d)
elif C == e:
    print("The multiplication of the numbers is :" , e)
elif C == f :
    print("The min number is :",f)
else :
    print("The max number is : ", g)

#2) weight convertor 
weight = float(input("Enter your weight : "))
unit = input("Kilograms or pounds ?? ( K or L):")
if unit =="K":
    weight == weight * 2.205
elif unit == "L":
    weight = weight / 2.205
else:
    print(  unit ," was not valid ")
print("Your weight is : ",weight , unit )

#3 Temperature convertor 
unit = input("Is this temperature is in celsius or Fahrenhit (C/F):")
temp = float(input("Enter the temperature: "))
if unit == "C":
    temp = round((9*temp) / 5 + 32, 1)
    print("The temperature in Fahremheit is:  " , temp)
elif unit == "F":
    temp = round((temp - 32) * 5 / 9 , 1)
    print(unit , "is an invalid unit of measurment")
#4) vaalidate user input exercise
""" 1.username is no more than 12 characters
2. username must not contain spaces
3. username must not contain digits """
username = input("Enter the username :")
if len(username) > 12:
    print("Your username can't be more than 12 characters ")
else:
    print("welcome ", username )
username.find(" ") == -1
if username.find(" " ) == -1:
    print("Username should not contain any spaces")
else:
    print("Welcome",username)
if username.isdigit() == "true":
    print("it contains digits so it is not eligible ")
else:
    print("it does not contain any  digits so it is eligible ")
#5) indexing 
Ashithi = "ABCDEFGHIJ"
print(Ashithi[2])
#starting index - end index - step 
print(Ashithi[0:4])
print(Ashithi[0:4:2])
print(Ashithi[2:])
print(Ashithi[-1])
print(Ashithi[-2])
print(Ashithi[-3])
print(Ashithi[-4])
print(Ashithi[-5])
print(Ashithi[-6])
print(Ashithi[-7])
print(Ashithi[-8])
print(Ashithi[-9])
print(Ashithi[-10])
