"""
a = " Hello, World!     "
a_hossza = len(a)
print("Az a hossza: ",a_hossza)
print(a.strip())
b = a.strip()
b_hossza = len(b)
print("A b hossza: ",b_hossza)"""


a = "hello,world,2222,3333"

print(a.split(","))
lista = a.split(",")
print(lista[3])
b = "44;303;2344;333;6236"
print(b.split(";"))
lista1 = b.split(";")
print(lista1[3])
for x in lista1:
    print(x)
szamlalo = 0    
for x in lista:
    print("A lista ",szamlalo, "-ik eleme ",x)
    szamlalo = szamlalo + 1