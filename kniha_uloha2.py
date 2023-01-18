import shutil

def pocet_hier(subor):
    hada_file = open(subor, "r")
    hada_citanie = hada_file.read()
    pocet=1
    for i in hada_citanie:
        if "\n" in i:
            pocet+=1

    return pocet

print(pocet_hier("hada.txt"))

def najdlz_hra(subor):
    hada_file = open(subor, "r")
    hada_citanie = hada_file.read()
    hada_list = hada_citanie.split()
    return max(hada_list, key=len)

print(najdlz_hra("hada.txt"))

def kopia(subor):

    shutil.copyfile(subor, "hada2.txt")

kopia("hada.txt")


def kompakt(subor):
    hada_file = open(subor, "r")
    hada_citanie = hada_file.read()
    komp=""
    pocet = {}
    hada_citanie2 = hada_citanie.replace("\n", "")
    for s in hada_citanie2:
        if s in pocet:
            pocet[s] += 1
        else:
            pocet[s] = 1

    for key in pocet:
        if pocet[key] > 1:
            komp += key + " " + str(pocet[key]) + " "
            with open("hada2.txt", "w") as hada2:
                hada2.write(komp)



print(kompakt("hada.txt"))