elemendid = []

#Lisame ELEMENDI juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    for element in elemendid:
        if nimetus in element.values():
            print("Element {} on juba olemas".format(nimetus))
            break
        else:
            elemendid.append({"nimetus": nimetus, "hind": hind, "kogus": kogus})
            print("Lisati ", str(nimetus))
            break

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
     for element in elemendid:
         if nimetus not in element.values():
             print("Element {} ei eksisteeri".format(nimetus))
             break
         else:
             return print("Element,", str(nimetus),  ",on loendis olemas.")
             break


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

print(loe_element("leib"))

