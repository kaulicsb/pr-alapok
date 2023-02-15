"""
keresznev = input("add meg a nevedet: ")
kor = int(input("add meg a korod: "))
if kor < 1:
    print(f"A kor alapján {keresznev} csecsemő")
if kor <= 6:
    print(f"A kor alapján {keresznev} kisgyerek")
if kor <= 12:
    print(f"A kor alapján {keresznev} gyerek")
if kor <= 16:
    print(f"A kor alapján {keresznev} serdölő")
if kor <= 25:
    print(f"A kor alapján {keresznev} ifjú")
if kor < 65:
    print(f"A kor alapján {keresznev} felnőtt") 
if kor >= 65:
    print(f"A kor alapján {keresznev} nyugdíjas")
"""

"""
szelesseg = input("szélesség: ")
magassag = input("magasság: ")
print(szelesseg*magassag)
if szelesseg > magassag:
    print("fekvő")
if szelesseg < magassag:
    print("álló")
if szelesseg == magassag:
"""














lista = [7,8,6,2,15,1,13,5,9,11,12,3,4]
for x in lista:
    if lista[0] > lista[0+1]:
         