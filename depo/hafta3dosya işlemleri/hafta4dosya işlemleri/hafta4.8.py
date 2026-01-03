class Ogrenci(): # Sınıf tanımlama
    def __init__(self,a,b,cc): # initialize/başlatma fonksiyonu
        self.adi = a
        self.soyadi = b
        self.numarasi = cc


# ogrenci1 = Ogrenci() # sınıftan nesne tanımlama
# ogrenci1.adi = "Bartu"
# ogrenci1.numarasi = 776
# ogrenci1.soyadi = "KARA"
ogrenci1 = Ogrenci("Bartu",776,"KARA") # sınıftan nesne tanımlama


print(type(ogrenci1))
print("öğrenci1 özelikleri\n",ogrenci1.adi, ogrenci1.soyadi, ogrenci1.numarasi)