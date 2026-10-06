# multiplication table of 10  
from os import replace


A = 10
for i in range(1, 101):
    print(A, "*", i, "=", A*i)

B = "ASHITHI"
print(B[0:4])
C = "WELCOME"
print(C[3:6])
D = "  ashu  "
print(D.upper())
E = "   ASHU  "
print(E.lower())
F = "     ASHU   "
print(F.strip())
G = "aSHITHI"
print(G.replace("a", "A"))
#Center()
H = "ASHITHIYADAV"
print(H.center(20,"o"))
#count()
I = "ASHITHIYADAV"
print(I.count("A"))
#encode()
J = "ASHITHIYADAV"
print(J.encode())
#Endswith()
K = "Karthik"
print(K.endswith("k"))
#find()
L = "KArthi"
print(L.find("t"))
#format()
M = "Abhi"
print(M.format())
# formate_map()
N = "Abhi"
print(N.format_map())