"""
szamoklista = [3, 21, 7, 63, 9, 27]
def minmax(szamoklista):
    min = szamoklista[0]
    max = szamoklista[0]
    for szam in szamoklista:
        if szam < min:
            min = szam
        if szam > max:
            max = szam

    print(f'A legkisebb szám a listában: {min} ')
    print(f'A legnagyobb szám a listában: {max} ')
minmax(szamoklista)
"""
#összegzés tétele

szamoklista = [3, 21, 7, 63, 9, 27]
osszeg = 0
for resz in szamoklista:
    osszeg = osszeg + resz
print(f"A héten ennyi értékesítés történt: {osszeg}")
atlag = None
atlag = osszeg / len(szamoklista)
print(f"a lista elemeinek átlaga :{atlag}")

