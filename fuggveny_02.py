# lower()  Az lower() metódus egy olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
def lower1():
    txt = "Hello my FRIENDS"

    x = txt.lower()

    print(x)
lower1()

# upper  A upper() metódus egy olyan karakterláncot ad vissza, amelyben minden karakter nagybetűs.
def upper1():
    txt = "Hello my friends"

    x = txt.upper()

    print(x)
upper1()

# .capitalize()  A .capitalize()  metódus egy karakterláncot ad vissza, ahol az első karakter nagybetű, a többi pedig kisbetű.
def capitalize1():
    txt = "hello, and welcome to my world."

    x = txt.capitalize()

    print (x)
capitalize1()

# endswith()  Az endswith() metódus True-t ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben pedig False-t.
def endswith1():
    txt = "Hello, welcome to my world."

    x = txt.endswith(".")

    print(x)
endswith1()

# find ()   A find() metódus megkeresi a megadott érték első előfordulását.  A find() metódus -1-et ad vissza, ha az érték nem található.  A find() metódus szinte megegyezik az index() metódussal, a különbség csak annyi, hogy az index() metódus kivételt jelent, ha nem található az érték. (Lásd a példát lent)
def find1():
    txt = "Hello, welcome to my world."

    x = txt.find("welcome")

    print(x)
find1()


# isalnum()  Az isalnum() metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, vagyis ábécé betűit (a-z) és számokat (0-9).  Példa olyan karakterekre, amelyek nem alfanumerikusak: (szóköz)!#%&? stb.
def isalnum1():
    txt = "Company12"

    x = txt.isalnum()

    print(x)
isalnum1()

# isalpha()  Az isalpha() metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (a-z).  Példa olyan karakterekre, amelyek nem ábécé betűi: (szóköz)!#%&? stb.
def isalpha1():
    txt = "CompanyX"

    x = txt.isalpha()

    print(x)
isalpha1()

# islower()  Az islower() metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False.  A számok, szimbólumok és szóközök nincsenek bejelölve, csak az ábécé karakte
def islower1():
    txt = "hello world!"

    x = txt.islower()

    print(x)
islower1()

# join()  A join() metódus az összes iterálható elemet veszi, és egyetlen karakterláncba egyesíti.  Elválasztóként egy karakterláncot kell megadni.
def join1():
    myTuple = ("John", "Peter", "Vicky")

    x = "#".join(myTuple)

    print(x)
join1()

# replace()  A replace() metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre.
def replace1():
    txt = "I like bananas"

    x = txt.replace("bananas", "apples")

    print(x)
replace1()

# rfind()   Az rfind() metódus megkeresi a megadott érték utolsó előfordulását.  Az rfind() metódus -1-et ad vissza, ha az érték nem található.   Az rfind() metódus majdnem megegyezik a rindex() metódussal. Lásd alább a példát.
def rfind1():
    txt = "Mi casa, su casa."

    x = txt.rfind("casa")

    print(x)
rfind1()

# rstrip()  Az rstrip() metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter.
def rstrip1():
    txt = "     banana     "

    x = txt.rstrip()

    print("of all fruits", x, "is my favorite")
rstrip1()

# startswith()  A startswith() metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik, ellenkező esetben False-t.
def startswith1():
    txt = "Hello, welcome to my world."

    x = txt.startswith("Hello")

    print(x)
startswith1()


# strip()  A strip() metódus eltávolítja a kezdő (szóköz az elején) és a záró (szóköz a végén) karaktereket (a szóköz az eltávolítandó alapértelmezett kezdőkarakter).
def strip1():
    txt = "     banana     "

    x = txt.strip()

    print("of all fruits", x, "is my favorite")
strip1()

# swapcase()  A swapcase() metódus egy olyan karakterláncot ad vissza, amelyben az összes nagybetű kisbetű, és fordítva.
def swapcase1():
    txt = "Hello My Name Is PETER"

    x = txt.swapcase()

    print(x)
swapcase1()

# title()  A title() metódus egy karakterláncot ad vissza, ahol minden szó első karaktere nagybetű. Mint egy fejléc vagy egy cím.   Ha a szó számot vagy szimbólumot tartalmaz, az utána lévő első betű nagybetűvé alakul.
def title1():
    txt = "Welcome to my world"

    x = txt.title()

    print(x)
title1()

# center()  A center() metódus középre igazítja a karakterláncot, és egy megadott karaktert használ (a szóköz az alapértelmezett) kitöltési karakterként.
def center1():
    txt = "banana"

    x = txt.center(200000000)

    print(x)
center1()