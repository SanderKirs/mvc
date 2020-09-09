elemendid = []

#Lisame ELEMENDI juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})


#Lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#Loome katse andmestiku
katse_elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus":20},
    {"nimetus": "piim", "hind":0.50, "kogus":15},
    {"nimetus": "vein", "hind":5.60, "kogus":5},
]
#Testime elementide lisamist
lisa_elemendid(katse_elemendid)
print(elemendid)

#Testime elemendi lisamist
lisa_element("kohupiim",0.90,15)
print(elemendid)