temp = 25
is_raning = False
if temp > 35 or temp < 0 or is_raning:
    print("The outdorr event is cancelled")
else:
    print("The outdoor event is still scheduled ")
#condtional expression :
x = int(input("Enter the number:"))
#print("eligible for voting "if x >= 18  else "Not eligible for voting")
result = "eligible for voting "if x >= 18  else "Not eligible for voting"
print(result)
# string methods
a = input("Enter you name:")
A = a.find("A")
B = a.isdigit()
C = a.upper()
D = a.lower()
E =a.isalpha() 
R = input("Enter Any alphabet:")
if R == A:
    print(A)
elif R == B:
    print(B)
elif R == C:
    print(C)
elif R == D:
    print(D)
else:
    print(E)