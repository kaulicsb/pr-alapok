"""
szoveg = "hello világ"
for karakter in szoveg:
    print(karakter,end="")

  
for szam in range(50,101,3):
    print(szam,end=" ")
print()

for szam in range(50,101,3):
    if szam % 2 == 0:
        print(szam,end=" ")
print()
for szam in range(50,101,3):
    if szam % 2 == 1:
        print(szam,end=" ") 

nev_kicsi = ""
nev = input("Kérem a nevedet: ")
for karakter in nev:
    nev_kicsi = nev_kicsi + karakter.lower()
print(nev_kicsi)
szamlalo = 0
for karakter in range(len(nev_kicsi)):
    if szamlalo == 0:
        print(karakter)"""