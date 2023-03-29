# ord()  Az ord() függvény egy megadott karakter unicode kódját reprezentáló számot adja vissza.
def ord1():
    x = ord("h")
    print(x)
ord1()

# chr()     A chr() függvény a megadott unicode-ot képviselő karaktert adja vissza.
def chr1():
    x = chr(97)    
    print(x)
chr1()

# min()  A min() függvény a legalacsonyabb értékű vagy a legalacsonyabb értékű elemet adja vissza az iterálható elemben.
def min1():
    x = min(5, 10, 12, 31)
    print(x)
min1()

# max()  A max() függvény a legmagasabb értékű vagy a legmagasabb értékű elemet adja vissza az iterálható elemben.
def max1():
    x = max(5, 10 ,31, 54, 22, 32)
    print(x)
max1()

# index()  Az index() metódus a pozíciót adja vissza a megadott érték első előfordulásakor.
def index1():
    fruits = ['apple', 'banana', 'cherry']
    x = fruits.index("cherry")  
    print(x)
index1()

# list()  A list() függvény egy lista objektumot hoz létre.
def list1():
    x = list(('apple', 'banana', 'cherry'))
    print(x)
list1()