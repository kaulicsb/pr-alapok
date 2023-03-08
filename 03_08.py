# Kaulics Balázs A 03_08
szam_sorozat = [15, 4, 5, 19, 2]
def megszamlalas():
    darab = 0
    x = 0
    for szam in szam_sorozat:
	      if x < szam:
		        darab = darab + 1

    print(f"A listában {darab} szám található") 
megszamlalas()