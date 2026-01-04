class Ogrenci:
    def __init__(self,xx,yy,zz="Normal"):
        self._ad = xx # public / her sınıfa, her yere açık
        self.no = yy
        self.__sd = zz # private/dışarıdan ulaşılamayan değişken.
        # Sadece kendi sınıfının içindeki metodlar ile ulaşılabilir.
   
    def saglikDurumu(self):
        return self.__sd + " (Özel bilgi)"    


ogrenci1 = Ogrenci("Efekan",458,"Alerjisi var")


# print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci1._ad} {ogrenci1.__sd}")
print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci1._ad} {ogrenci1.saglikDurumu()}")


ogrenci2 = Ogrenci("Ahmet", 695, "İnsülin direnci var")
print(f"\n\nÖğrenci bilgisi:\nAdı:{ogrenci2._ad} {ogrenci2.saglikDurumu()}")