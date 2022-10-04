# Első feladat dk9 tankönyv
"""
IDEI_EV = 2022
print(type(IDEI_EV))
print('Az idei év:',IDEI_EV, sep='--->')
felhasznalo_kora = input("Hány éves vagy?")
print(type(felhasznalo_kora))0
print('Te most',felhasznalo_kora,'éves vagy')
felhasznalo_kora = int(felhasznalo_kora)
szuletesi_ev = IDEI_EV - felhasznalo_kora
print('Ekkor születtél:',szuletesi_ev,'.',sep='')
print(type(felhasznalo_kora))
felhasznalo_kora = str(felhasznalo_kora)
print(type(felhasznalo_kora))
print('És milyen ' + felhasznalo_kora + ' évesnek lenni?')
print('És milyen',felhasznalo_kora,'évesnek lenni?')
"""




# Második program
gondolt_szam = 4
tipp = input('Gondoltam egy számra. Tippeld meg!')
tipp = int(tipp)
if tipp == gondolt_szam:
    print('Ügyes vagy!')
    print('Gratulálok')

if tipp > gondolt_szam:
    print('Nagyobb számot adtál meg')

if tipp < gondolt_szam:
    print('Kisebb számot adtál meg')
