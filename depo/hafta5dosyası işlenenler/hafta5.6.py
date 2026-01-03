dosya = open("rehber.dat")
print(" KAYIT LİSTESİ ")
print("===============")
print("Adı\t\tTelefonu")
okunan = dosya.readlines()
for a in okunan:
    satir = a.strip().split("#")
    print(satir[0],"\t",satir[1])
