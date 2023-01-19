def pocet_merani(subor):
    metero = open(subor, 'r')
    meranie = len(metero.readlines())
    print("Počet meraní je", meranie)

pocet_merani("metero.txt")

def teploty(subor):
    metero = open(subor, 'r', encoding="utf-8")
    konec=[]
    x = ""
    for i in metero:
        splitovanie = i.split()
        x = splitovanie[3].replace('\U00002013', '-')
        konec.append(float(x))
        konec.sort()

    print("Najvyššia teplota je: " + str(konec[2]))

def priemer(subor):
    metero = open(subor, 'r', encoding="utf-8")
    konec = []
    x = ""

    for i in metero:
        splitovanie = i.split()
        x = splitovanie[3].replace('\U00002013', '-')
        konec.append(float(x))

    print("Priemerná teplota je: " + str((konec[0] + konec[1] + konec[2]) / 3))

def stanica(subor):
    metero = open(subor, 'r', encoding="utf-8")
    konec = []
    x = ""

    for i in metero:
        splitovanie = i.split()
        x = splitovanie[3].replace('\U00002013', '-')
        konec.append(float(x))
        konec.sort()
    with open(subor) as sub:
       for line in sub:
           if str(konec[2]) in line:
               print(line[0] + line[1] + line[2])

priemer("metero.txt")
teploty("metero.txt")
stanica("metero.txt")

