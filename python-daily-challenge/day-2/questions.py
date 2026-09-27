#excercise - 1
import math 
radius = float(input("Enter the radius of circle: "))
area = math.pi *radius * radius 
print("The area of  the circle is : " , area)
circumference = 2*math.pi * radius
print("The circumference of the circle is :", circumference) 
A = int(input("Enter the side of A:"))
B = int(input("Enter the side of B:"))
c = math.sqrt(pow(A,2) + pow(B,2))
print("The lenght of the hypothenuse is :" , c)
#excerise - 2 
# to check wheather the customer is valid for credit card or not 
age = int(input("enter the age :"))
if (age >= 18):
    print("You are eligible for credit card")
else:
    print("You should be 18 or 19 above to get a credit card")

# 2 question 
# pass or fail 
x = int(input("Enter your marks:"))
if x >= 40:
    print("You are pass")
else:
    print("You are fail")
# 3 question 
# even or odd:
number = int(input("enter the number:"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#4 voting eligibility 
x = input("Enter your name:")
y = int(input("Enter your age:"))
if y >= 18:
    print("Your are eligible for voting")
else:
    print("You need to be 18 or above 18 to vote ")
#4 traffic lioght simulator 
print("Traffic light code : 1 - Red , 2- Yellow , 3 - Green")
light = int(input("Enter the traffic light color code "))
if light == 1:
    print("Stop the vehicle")
elif light == 2:
    print("Get ready to start ")
else:
    print("Go and drive safely")
#5 Number classifier 
number = int(input("Enter a number:"))
if number > 0:
    print("The number is positive")
elif number <0:
    print("The number is negative")
elif number == 0 :
    print("The number is zero")
#6 Grade calculator
marks = int(input("Enter your marks:"))
if marks >= 800 :
    print("You got a grade A")
elif marks >= 600 and marks < 800:
    print("You got grade B")
elif marks >= 400 and marks < 600:
    print("You got grade C")
else:
    print("You got grade D")
#7) leap year calculator 
year = int(input("Enter the year :"))
if year % 4 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")
#8) Find the largest 
A = int(input("Enter the first number:"))
B = int(input("Enter the second number:"))
C = int(input("Enter the third number:"))
if A > B and A > C:
    print("The largest number is A")
elif B>A and B>C:
    print("The largest number is B")
elif C>A and C>B:
    print("The Largest number is C")
else:
    print("All numbers are equal")

#9 Hacker rank "weird number challenge" 
n = int(input("Enter a number:"))
if n % 2 != 0:
    print("The given number is odd")
elif n % 2 == 0 and n <= 5:
    print(" n is even and Not Weird")
else:
    print("n is even and Not Weird")