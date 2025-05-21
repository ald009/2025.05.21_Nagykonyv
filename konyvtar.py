from nagykonyv import konyv

class Konyvtar:
    def __init__(self):
        self.konyvek = []
        self.olvasas()

    def olvasas(self):
        with open("konyvek.txt", "r", encoding="utf-8") as fajl:

            line.readline()
            for sor in fajl:
                adatok = sor.strip().split(";")
                nev = adatok[0]
                szul_ev = int(adatok[1])
                hal_ev = int(adatok[2])
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezes = adatok[5]

                konyvek.append(konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))
            