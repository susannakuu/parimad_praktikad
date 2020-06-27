def nimekiri_lugudest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore') # avab faili, mida käsitletakse
    albumid = [] # teeb albumid nimekirjaks
    for rida in fail: # loeb iga rea eraldi ning kutsub järgmised käsklused, loob tsükli
        rida_elementide_kaupa = rida.split('\t') # iga kord kui failis on rohkem kui üks tühik, ".split('\t')" teeb selle ueeks lahtriks
        album = rida_elementide_kaupa[1] # võtab ainult albumid ehk tekstijupatsi, mis on peale esimest (rida_elementide_kaupa[0]) lahtrit.
        albumid.append(album) # lisab õpilaste nimed listi "albumid"
        if len(albumid) > 1: # kui albumis on sama rida rohkem kui üks siis...
            if albumid[-2] != albumid[-1]: # võrdleb praegust rida järgmisega
                print() # ->
                print("-------------------------------------------") # kui praegune rida pole järgmisega sarnane, siis algab uus tsükkel
                print() # ->
        print(rida) # väljastab kastuajale praeguse rea
    fail.close() # fail pannakse kinni, et programm täielikult lõpetada.
    
# JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON

# kuvab kõik albumid ning nende autorid
def kõik_albumid():
    fail1 = open("a.txt", "w", encoding='utf-8') # avab faili kuhu spetsiifiline osa teisest failist kirjutatakse
    fail2 = open("albumid.txt", encoding='utf-8', errors ='ignore') # avab faili, kust kõik andmed üldse kätte saadakse
    for rida in fail2: # loeb iga rea eraldi
        rida_element = rida.split('\t') # määrab rida_element'i selleks, mis võtab 
        fail1.write(rida_element[0] + " - " + rida_element[1] + '\n') # võtab igalt realt autori ning albumi nime ning ühendab need sidekriipsuga
    fail1.close() # paneb faili kinni, et teha teistele asjadele ruumi
    kõikalbumid() # kutsub järgmise funktsiooni
def kõikalbumid(): # funktsioon korduvate ridade eemaldamiseks
    import os # teeb failide kustutamise võimalikuks
    lines_seen = set() # loob väikse koguse, kuhu saab sõnesid/ridasid spetsiifilise koodi abil lisada
    outfile = open("b.txt", "w") # loob faili, kuhu tulemus kirjutatakse
    for line in open("a.txt", "r"): # avab eelmises funktsioonis loodud nimekirja lugedes iga rida eraldi
        if line not in lines_seen: # kui rida pole koguses...
            outfile.write(line) # loeb rea ning lisab selle faili "b.txt"...
            lines_seen.add(line) # ja paneb rea kogusesse, et selle taoliseid ridasid ei saaks enam kasutada.
    outfile.close() # paneb faili kinni, et Python saaks järgmisena TERVE faili ette lugeda
    f = open("b.txt", "r", encoding='utf-8').read() # avab failile lugemiseks
    print(f) # loeb faili ette
    os.remove("a.txt") # kustutab üleliigse
    os.remove("b.txt") # kustutab üleliigse
    
# JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON

# edasi teeme otsingu
def otsing_albumid(otsitav_album):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore') # avab faili
    albumid = [] # teeb nimekirja nimega "albumid"
    for rida in fail: # loob tsükli
        rida_elementide_kaupa = rida.split('\t') # eraldab albumid, artistid, aastaja ning loo nime.
        artist = rida_elementide_kaupa[0] # määrab esimese lahtri nimele "artist"
        album = rida_elementide_kaupa[1] # määrab teise lahtri nimele "album"
        albumid.append(album) # paneb albumite nimed nimekirja
        aasta = rida_elementide_kaupa[2] # määrab kolmanda lahtri nimele "aasta"
        lugu = rida_elementide_kaupa[3] # määrab neljanda lahtri nimele "lugu"
        '''
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("-------------------------------------------")
                print()
                '''
        if(album == otsitav_album): # kui kasutaja sisestas albumi nime ja see läheb kokku nimekirjas olevaga...
            print(rida) # väljastatakse album koos kõige muuga kasutajale
    fail.close() # fail pannakse kinni, et programm täielikult lõpetada
    
# JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON JÄRGMINE FUNKTSIOON

# väljastab ainult lugude nimed
def loo_nimed():
    fail1 = open("a.txt", "w", encoding='utf-8') # loob uue faili, kuhu loo nimed lähevad
    fail2 = open("albumid.txt", encoding='utf-8', errors ='ignore') # teeb lahti faili nimega "albumid.txt"
    for rida in fail2: # käseb iga rida täpselt niimodi kohelda:
        rida_element = rida.split('\t') # määrab "rida_element" nimeks sellele, mis jagab kõik andmed lahtriteks
        fail1.write(rida_element[0] + " - " + rida_element[3] + '\n') # kirjutab faili "a.txt" esimese ning neljanda lahtri.
    fail1.close() # sulgeb "a.txt", et teistele asjadele ruumi teha
    loonimed() # kutsub järgmise funktsiooni
def loonimed():
    import os # moodul failide kustutamiseks
    lines_seen = set() # loob nähtud ridade listi
    outfile = open("b.txt", "w") # loob uue faili, kuhu lõplikud tulemused kirjutatakse
    for line in open("a.txt", "r"): # avab faili "a.txt", kus andmed loetakse
        if line not in lines_seen: # kui rida pole listis näha...
            outfile.write(line) # kirjutatakse see faili "b.txt"
            lines_seen.add(line) # lisatakse see listi, et seda enam kasutada ei saaks
    outfile.close() # fail pannakse kinni, et ruumi teha teistele asjadele
    f = open("b.txt", "r", encoding='utf-8').read() # avatakse uuesti "b.txt", kuid seekord et sealt andmed ette saaks lugeda
    print(f) # väljastatakse kõik failis "b.txt" kasutajale
    os.remove("a.txt") # kustutab liigse
    os.remove("b.txt") # kustutab liigse

# menüü kasutajale
print("1 - kõik albumid ja lood albumite kaupa")
print("2 - kõik albumid")
print("3 - albumi otsing")
print("4 - lugude otsing")
print()
valik = int(input("Sisesta oma valik: "))
if(valik == 1):
    nimekiri_lugudest() # kui kasutaja sisestas "1" siis kutsub programm funktsiooni "nimekiri_lugudest()"
if(valik == 2):
    kõik_albumid() # kui kasutaja sisestas "2" siis kutsub programm funktsiooni "kõik_albumid()"
if(valik == 3):
    otsitav_album = input("Millist albumit otsid: ")
    otsing_albumid(otsitav_album) # kui kasutaja sisestas "3" siis kutsub programm funktsiooni "otsing_albumid()"
if(valik == 4):
    loo_nimed() # kui kasutaja sisestas "4" siis kutsub programm funktsiooni "loo_nimed()"