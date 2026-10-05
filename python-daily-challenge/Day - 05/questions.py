'''N = int(input("Enter the number : " ))
while N < 1 or N > 10:
    print("please enter numbers between 1-10")
    N = int(input("Enter the number : "))
print("Your number is" , N)


#python compound intreset calculator 
r = int(input("Enter the rate of intrest :"))
n = int(input("Enter the number :"))
t = int(input("Enter the number of time periods elapsed :"))
p = int(input("Enter the initial principal balance :"))
A = float(p * (1+r/n)**t)
print(A)
'''

Rate = 0
time = 0 
principal = 0 
while time <= 0 :
    time = float(input("Enter the time :"))
    if time <= 0:
        print("Time cannot be less than  0 or equal to zero")
while Rate <= 0:
    Rate = float("Enter the Rate :")
    if Rate <= 0 :
        Print("Rate cannot be less than 0 or equal to Zero ")
while principal <= 0:
    print("Enter the principal")
    if principal <= 0:
        print("pricipal cannot be less than 0 ir equal to zero")
total = principal * ( 1+ rate/100)**time

jota ,fod , lean , ray