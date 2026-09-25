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