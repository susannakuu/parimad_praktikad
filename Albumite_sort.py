def nimekiri_lugudest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("-------------------------------------------")
                print()
        print(rida)
    fail.close()
    
def nimekiri_albumitest():
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = []
    artistid = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        artistid.append(artist)
        album = rida_elementide_kaupa[1]
        albumid.append(album)
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        if len(albumid) > 1:
            if artistid[-2] != artistid[-1]:
                print()
                print(artist)
                print("----------")
                
            if albumid[-2] != albumid[-1]:
                print(album)
    fail.close()
# edasi teeme otsingu
def otsing_albumid(otsitav_album):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    albumid = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
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
        if(album == otsitav_album):
            print(rida)
    fail.close()
    
def otsing_lood(otsitav_lugu):
    fail = open("albumid.txt", encoding='utf-8', errors ='ignore')
    lood = []
    for rida in fail:
        rida_elementide_kaupa = rida.split('\t')
        artist = rida_elementide_kaupa[0]
        album = rida_elementide_kaupa[1]
        
        aasta = rida_elementide_kaupa[2]
        lugu = rida_elementide_kaupa[3]
        lugu2 = lugu.replace("\n", "")
        lood.append(lugu2)
        '''
        if len(lugu2) > 1:
            if lood[-2] != lood[-1]:
                print()
                print("-------------------------------------------")
                print()
                '''
        if(lugu2 == otsitav_lugu):
            print(rida)
    fail.close()

# menüü kasutajale
print("1 - kõik albumid ja lood albumite kaupa")
print("2 - kõik albumid")
print("3 - albumi otsing")
print("4 - lugude otsing")
print()
valik = int(input("Sisesta oma valik: "))
if(valik == 1):
    nimekiri_lugudest()
if (valik == 2):
    print("Esitaja ja tema albumid on eraldatud kriipsudega!")
    nimekiri_albumitest()
if(valik == 3):
    otsitav_album = input("Millist albumit otsid: ")
    otsing_albumid(otsitav_album)
if(valik == 4):
    otsitav_lugu = input("Millist lugu otsid: ")
    otsing_lood(otsitav_lugu)
