dosya = "rehber.txt"

def ekle():
    ad = input("Ad: ")
    tel = input("Tel: ")
    para = input("Para: ")
    open(dosya, "a").write(ad + "," + tel + "\n")
    print("Eklendi")

def listele():
    print("\n--- KAYITLAR ---")
    print(open(dosya).read())

def ara():
    isim = input("Aranacak ad: ").lower()
    for s in open(dosya):
        ad, tel, para, = s.strip().split(",")
        if isim == ad.lower():
            print("Bulundu:", ad, tel)
            return
    print("Bulunamadı")

def sil():
    isim = input("Silinecek ad: ").lower()
    satirlar = open(dosya).readlines()
    yeni = []
    silindi = False

    for s in satirlar:
        ad = s.split(",")[0].lower()
        if ad != isim:
            yeni.append(s)
        else:
            silindi = True

    open(dosya, "w").writelines(yeni)
    print("Silindi" if silindi else "Bulunamadı")

def duzenle():
    isim = input("Düzenlenecek ad: ").lower()
    satirlar = open(dosya).readlines()
    yeni = []
    bulundu = False

    for s in satirlar:
        ad, tel = s.strip().split(",")
        if ad.lower() == isim:
            ad = input("Yeni ad: ")
            tel = input("Yeni tel: ")
            para = input("Yeni para: ")
            yeni.append(ad + "," + tel + "\n")
            bulundu = True
        else:
            yeni.append(s)

    open(dosya, "w").writelines(yeni)
    print("Güncellendi" if bulundu else "Bulunamadı")

def sayi():
    print("Toplam kayıt:", len(open(dosya).readlines()))

while True:
    print("""
1-Ekle
2-Listele
3-Ara
4-Sil
5-Düzenle
6-Kayıt sayısı
7-Çıkış
""")
    s = input("Seçim: ")

    if s == "1": ekle()
    elif s == "2": listele()
    elif s == "3": ara()
    elif s == "4": sil()
    elif s == "5": duzenle()
    elif s == "6": sayi()
    elif s == "7": break

input()