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
                helyezes = int(adatok[5])

                self.konyvek.append(konyv(nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes))
        
    def db(self):
        print("3.2. feladat: Az állománybban",len(self.konyvek), "db könyv adatai szerepelnek.")
    
    def legjobbhu(self):
        illat = 0
        legjobb = 100
        for i, a in enumerate(self.konyvek):
            if a.nemzetiseg == "magyar":
                if legjobb > a.helyezes:
                    legjobb = a.helyezes
                    illat = i
        print("3.3 feladat: A legjobb helyezést elért magyar könyv:",self.konyvek[illat].nev,":",self.konyvek[illat].cim )
    
    def nemet(self):
        nem = True
        for i in self.konyvek:
            if i.nemzetiseg == "német":
                nem = False
                break
        print("3.4 feladat : A listában" ,"NEM" if nem == True else "", "szerepel német író könyve.")

    def kilencven(self):
        print("3.5 feladat: 90 évesnél idősebb írók:")
        volt = []
        for f in self.konyvek:         
            if f.hal_ev - f.szul_ev > 90:
                 if f.nev not in volt: 
                    print(f.nev)
                    volt.append(f.nev)
                        

tar = Konyvtar()
tar.db()
tar.legjobbhu()
tar.nemet()
tar.kilencven()

            