elemendid = []

#Lisame ELEMENDI juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        print("Element {} juba eksisteerib".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})

#Lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#Loeme elemendid korraga
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid

#loeme konkreetne element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei eksisteeri".format(nimetus)
    else:
        return elemendid[nimetused.index(nimetus)]

def uuenda_element(nimetus,hind,kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Element {} ei eksisteeri".format(nimetus)
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Element {} ei eksisteeri".format(nimetus)
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])

def kustuta_elemendid():
    global elemendid
    elemendid.clear()

def main():

    #Loome katse andmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind": 0.80, "kogus": 20},
        {"nimetus": "piim", "hind": 0.50, "kogus": 15},
        {"nimetus": "vein", "hind": 5.60, "kogus": 5},
    ]
    #Testime elementide lisamist
    lisa_elemendid(katse_elemendid)
    print(elemendid)

    #Testime elemendi lisamist
    lisa_element("kohupiim", 0.90, 15)
    #print(elemendid)

    lisa_element("leib", 0.80, 5)
    print(elemendid)

#Käivitamine
if __name__ == "__main__":
    main()
#ühe elemendi lugemine
#print(loe_element("leib"))

lisa_element("vein", 0.50, 5)

#Testime elemendi uuendamist
uuenda_element("vein", 0.15, 7)
print(loe_element("vein"))

#Testime ühe elemendi kustutamist
kustuta_element("vein")
print(elemendid)

#Testime kõikide elementide kustutamist
kustuta_elemendid()
print(elemendid)