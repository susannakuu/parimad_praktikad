# valik 1 - programm edastab kasutajale kõik lood, albumid ja muu, mis failis näha on.
def nimekiri_lugudest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = [] # loob nimekirja "albumid.txt" jaoks
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t') # iga kord kui failis on rohkem kui üks tühik, ".split('\t')" teeb selle uueks lahtriks
        artist = rida_elementide_kaupa[0] # lahter autorite jaoks
        album = rida_elementide_kaupa[1] # lahter albumite jaoks
        albumid.append(album) # lisab ainult albumid eelnevalt loodud nimekirja nimega "albumid"
        aasta = rida_elementide_kaupa[2] # lahter aastaaegade jaoks
        lugu = rida_elementide_kaupa[3] # lahter loonimede jaoks
        if len(albumid) > 1: # kui albumis on sama rida rohkem kui üks siis...
            if albumid[-2] != albumid[-1]: # võrdleb praegust rida järgmisega
                print()
                print("-------------------------------------------") # kui praegune rida pole järgmisega sarnane, siis algab tsükkel uuesti
                print()
        print(rida) # väljastab tulemuse kasutajale
    fail.close() # kui enam pole ridu mida saaks kasutajale edastada, siis programm paneb faili kinni.

# valik 2 - programm edastab kasutajale kõik albumid ning nende autorid
def nimekiri_albumitest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    
    albumid = []
    # loob kaks erinevat nimekirja, et need hiljem korduma ei hakkaks
    artistid = []
    
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        artistid.append(artist)
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        if len(albumid) > 1: # kui albumis on sama rida rohkem kui üks siis...
            if artistid[-2] != artistid[-1]: # võrdleb praegust rida järgmisega
                print() # lihtsalt tühi rida, et ilusam välja näeks
                print(artist) # väljastab autori nime
                print("----------")
                
            if albumid[-2] != albumid[-1]:
                print(album)
                # väljastab kõik autori albumid, kui neid on rohkem kui üks, sest need on failis ilusti järjes
                # kui üks autor kordub kaks korda erinevates kohtades koodis, ei näe see nii ilus välja
    fail.close() # kui rohkem pole midagi kasutajale edastada, pannakse fail kinni
    
# edasi teeme otsingu
def otsing_albumid(otsitav_album):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = [] # loob nimekirja "albumid.txt" jaoks
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t') # iga kord kui failis on rohkem kui üks tühik, ".split('\t')" teeb selle uueks lahtriks
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        '''
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("-------------------------------------------")
                print()
                '''
        if(album == otsitav_album): # kui failis olev tekst läheb kasutaja sisestatud tekstiga kokku...
            print(rida) # edastatakse kõik albumi detailid kasutajale
    fail.close() # ja kui programmil pole enam midagi edastada, paneb see "albumid.txt" kinni, et see ei raiskaks ruumi
    
def otsing_lood(otsitav_lugu):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    lood = [] # loob nimekirja "albumid.txt" jaoks
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t') # iga kord kui failis on rohkem kui üks tühik, ".split('\t')" teeb selle uueks lahtriks
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        lugu2 = lugu.replace("\n", "") # teeb loo leidmise võimalikuks
        '''
        if len(lugu2) > 1:
            if lood[-2] != lood[-1]:
                print()
                print("-------------------------------------------")
                print()
                '''
        if(lugu2 == otsitav_lugu): # kui real olev loo nimi läheb kokku kasutaja sisestatuga...
            print(rida) # väljastab programm rea kasutajale
    fail.close() # paneb faili kinni, et ruumi säästa

# menüü kasutajale
print("1 - kõik albumid ja lood albumite kaupa")
print("2 - kõik albumid")
print("3 - albumi otsing")
print("4 - lugude otsing")
print()
valik = int(input("Sisesta oma valik: "))
if(valik == 1): 
    nimekiri_lugudest() # kui kasutaja sisestas "1" siis kutsub programm funktsiooni "nimekiri_lugudest()"
if (valik == 2):
    print("Esitaja ja tema albumid on eraldatud kriipsudega!")
    nimekiri_albumitest()  # kui kasutaja sisestas "2" siis kutsub programm funktsiooni "nimekiri_albumitest()"
if(valik == 3):  
    otsitav_album = input("Millist albumit otsid: ")
    otsing_albumid(otsitav_album) # kui kasutaja sisestas "3" siis kutsub programm funktsiooni "otsitav_album()"
if(valik == 4):
    otsitav_lugu = input("Millist lugu otsid: ")
    otsitav_lugu = otsitav_lugu.title() # kui kasutaja ei kirjuta iga sõna suure tähega, siis tavaliselt ei laseks programm tal lugu leida, kuid see teeb loo leidmise kergemaks
    otsing_lood(otsitav_lugu) # kui kasutaja sisestas "4" siis kutsub programm funktsiooni "otsitav_lugu()"