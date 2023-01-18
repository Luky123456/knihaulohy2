def pocet_merani(subor):
    metero = open(subor, 'r')
    meranie = len(metero.readlines())
    print("Počet meraní je", meranie)

pocet_merani("metero.txt")

def teploty(subor):
    metero = open(subor, 'r', encoding="utf-8")
    konec = " "

    for i in metero:
        splitovanie = i.split()
        konec += splitovanie[3] + " "
        print(konec)

teploty("metero.txt")

