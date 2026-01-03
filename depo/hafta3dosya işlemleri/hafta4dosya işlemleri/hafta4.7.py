a = 12
b = "Vektörel"
print(b)
print(type(a))

class Ogrenci:
    adi = "Mustafa"
    soyadi = "KARA"
    numarasi = 470

ogrenci1 = Ogrenci()
ogrenci1.adi = "Bartu"
ogrenci1.numarasi = 776

aa = Ogrenci()
aa.adi = "Hüseyin"
aa.numarasi = 987

print("Öğrenci Bilgisi: ",Ogrenci.numarasi, Ogrenci.soyadi)
print(type(Ogrenci))
print(type(ogrenci1))
print(type(aa))