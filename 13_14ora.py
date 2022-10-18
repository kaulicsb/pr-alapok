
"""
szam1 = int(input("Kérek egy számot"))
szam2 = int(input("Kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1")
if szam1 == szam2:
    print("szam1 megegyezik a szam2-vel")
    """
    #----------------------------------------------------------------------------
"""
szam1 = int(input("Kérek egy számot"))
szam2 = int(input("Kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
elif szam1 == szam2:
    print("szam1 megegyezik a szam2-vel")

"""
#----------------------------------------------------------------------------
"""
szam1 = int(input("Kérek egy számot"))
szam2 = int(input("Kérek egy másik számot"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1")
else szam1 == szam2:
    print("szam1 megegyezik a szam2-vel")
    """
    #----------------------------------------------------------------------------
"""
x = None
print(x)
print(type(x))

if x:
    print("Do you think None is True?")
elif x is False:
    print("Do you think None is False?")
else:
    print("None is not True, or False, None is just None..."+) 
    
    """
#----------------------------------------------------------------------------

"""
jegy = input("Kérek egy osztályzatot")
if jegy == "1":
    print("elégtelen")
elif jegy == "2":
    print("elégséges")
elif jegy == "3":
    print("közepes")
elif jegy == "4":
    print("jó")
elif jegy == "5":
    print("jeles")
else:
    print("nem rendes osztályzat")
"""
"""
#----------------------------------------------------------------------------
#bekérek egy pozitív egész számot, irassuk ki h paros vagy paratlan
szam = int(input("Kérek egy pozitív egész számot "))
if szam % 2 == 0:
    print("A szám páros")
else:
    print("A szám páratlan")  

    """

#----------------------------------------------------------------------------
"""
import random

gondolt_szam = random.randint(1,6)
print('Súgok:', gondolt_szam)
tipp = int(input("tippelj egy számot"))
if gondolt_szam == tipp:
    print("jól tippeltél")
else: 
    print("nemjól tippeltél")
    """
    #----------------------------------------------------------------------------
#generáljunk egy számot 1-1000 között , irassuk ki a számot, ha őáros és kisebb mint 500 ha nem akkor a számom nem felelt meg a feltételeknek
"""
import random

szam = random.randint(1,1000)
print(szam)
if not(szam % 2 == 0) and szam <= 500:
    print("jó")
else:
    print("nem jó")
    """