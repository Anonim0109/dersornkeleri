class Ogrenci(): # Sınıf tanımlama
    def __init__(aa,a,b,cc): # initialize/başlatma fonksiyonu
        aa.adi = a
        aa.soyadi = b
        aa.numarasi = cc


    def bilgiVer(kendi):
        return f"\n\nÖğrenci bilgisi:\n{kendi.adi},{kendi.numarasi},{kendi.soyadi}"


ogrenci1 = Ogrenci("Bartu","KARA",985) # sınıftan nesne tanımlama


print(type(ogrenci1))
print("\n\nÖğrenci1 özelikleri\n",ogrenci1.adi, ogrenci1.soyadi, ogrenci1.numarasi)


print(ogrenci1.bilgiVer())


ogrenci3 = Ogrenci("Emir", "AKYOL", 342)
print(ogrenci3.bilgiVer())