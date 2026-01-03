ad = "Efekan"
tc = 20222241528
print(type(tc))
print(type(ad))
#  veri tipi, sınıf ve nesne kavramı
ogrenciler = ["Hüseyin","Emre","Bartu"]
print(type(ogrenciler))


# ogrenci = "Emir"
# ogrenci.ad = "Emir"
# ogrenci.nu = "452"


class Ogrenci():
    ad = "--"
    nu = "00"


ogrenci1 = Ogrenci()
ogrenci1.ad = "Emir"
ogrenci1.nu = 888
print(ogrenci1.ad, ogrenci1.nu)
print(type(ogrenci1))