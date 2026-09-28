#While loop :
'''n = input("Enter your name :")
if n == "":
    print("You did not enter your name")
else:
    print(f"Hello {n}")'''
name = input("Enter your name :")
while name == "":
    print("You did not entered any name ")
    name = input("Enter your name :")
print(f"Hello {name}" )
# until we enter the name it will repaet the loop because we used while loop one conditoin should become true for sure then it will jump to next