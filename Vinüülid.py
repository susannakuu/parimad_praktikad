
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

