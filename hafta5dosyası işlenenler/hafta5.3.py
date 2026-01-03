
# nesne tanımlama
class Ogrenci():
    def __init__(self,adi,num):
        self.ad = adi
        self.nu = num


# ogrenci1 = Ogrenci()
# ogrenci1.ad = "Emir"
# ogrenci1.nu = 888
ogrenci1 = Ogrenci("Ahmet",666)


print(ogrenci1.ad, ogrenci1.nu)
print(type(ogrenci1))