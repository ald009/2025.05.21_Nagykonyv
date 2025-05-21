from nagykonyv import konyv

class Konyvtar:
    def __init__(self):
        self.konyvek = []
        self.olvasas()

    def olvasas(self):
        with open("konyvek.txt", "r", encoding="utf-8") as fajl:

            fajl.readline()
            for sor in fajl:
                adatok = sor.strip().split(";")
                nev = adatok[0]
                szul_ev = int(adatok[1])
                hal_ev = int(adatok[2]) if adatok[2] else 2005
                nemzetiseg = adatok[3]
                cim = adatok[4]
                helyezes = adatok[5]

                self.konyvek.append(konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))
        
    def db(self):
        print("3.2. feladat: Az állománybban",len(self.konyvek), "db könyv adatai szerepelnek.")
tar = Konyvtar()
tar.db()


            