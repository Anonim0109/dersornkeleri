a = 5
ogrenci = {"adi":"berk","tc":"454545"}
#print("a :", a, type(a))
print("ogrenci1 :", ogrenci, type(ogrenci))

class ogrenci():
    adi = "--"
    tc = "0000"

ogrenci2 = ogrenci()

print(ogrenci2.adi)

ogrenci2.adi = "emir"
print("ogrenci2.adi:",ogrenci.adi)

ogrenci3 = ogrenci()
ogrenci3.adi = "bartu"

print("ogrenci3.adi :", ogrenci3.adi)
print("ogrenci3.tc :", ogrenci3.tc)
ogrenci3.tc = "454545"
print("ogrenci3.tc :",ogrenci.tc)
