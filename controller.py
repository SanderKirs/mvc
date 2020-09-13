class Controller:
    def __init__(self, mudel, vaade):
        self.mudel = mudel
        self.vaade = vaade

    #Elementide kuvamine
    def kuva_elemendid(self):
        elemendid = self.mudel.loe_elemendid()
        self.vaade.kuva_elemendid(elemendid)


    #Elemendi kuvamine
    def kuva_element(self, nimetus):
        element = self.mudel.loe_element(nimetus)
        self.vaade.kuva_element(nimetus, element)

    #Elemendi lisamine
    def lisa_element(self, nimetus, hind, kogus):
        if(hind <= 0):
            print("Hind peab olema suurem kui 0")
        elif(kogus <= 0):
            print("Kogus peab olema suurem kui 0")
        else:
            self.mudel.lisa_element(nimetus, hind, kogus)
            self.vaade.lisa_element(nimetus, hind, kogus)



    #Elemendi uuendamine
    def uuenda_element(self, nimetus, hind, kogus):
        if (hind <= 0):
            print("Hind peab olema suurem kui 0")
        elif (kogus <= 0):
            print("Kogus peab olema suurem kui 0")
        else:
            vana_element = self.mudel.loe_element(nimetus)
            self.mudel.uuenda_element(nimetus, hind, kogus)
            self.vaade.uuenda_element(nimetus, vana_element['hind'], vana_element['kogus'], hind, kogus)


    #Elemendi kustutamine
    def kustuta_element(self, nimetus):
        self.mudel.kustuta_element(nimetus)
        self.vaade.kustuta_element(nimetus)