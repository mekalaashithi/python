#Exercise questions 
# 1)Rectangle area and permeter 
lenght = float(input("Enter the length of the rectangle :"))
Breadth = float(input("Enter the breadth of the rectangle :"))
Area = lenght * Breadth
perimeter = 2 * ( lenght + Breadth)
print(Area)
print(perimeter)

#Excercise 2) Shopping cart program
iteam = input("What iteam would you like to buy? ")
price = float(input("What is the price of the iteam? "))
quantity = int(input("How many would you like to buy?"))
total = price * quantity
print("The total cost of your shopping cart is" , total)
#Exercise 3) Mablibs game 
adjective1 = input("Enter an adjective:")
adjective2 = input("Emter another adjective ")
noun2 = input("Enter a noun:")
verb1 = input("Emter a verb:")
print("Fill in the blanks to create a funny story!")
print("TOday i went to a {adjective1} zoo.")
print("In a exhibit i saw a {noun2}")
print("{noun2} was {adjective2} and {verb1}")
print("I was {adjective3}")
