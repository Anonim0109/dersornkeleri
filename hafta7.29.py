class Hesap:
    def __init__(self, ad, no, bakiyesi,komisyon=5):
        self.isim = ad
        self.numara = no
        self.__bakiye = bakiyesi # private prop = kontrolü (değişiklik) sınıf içerisinden yapılan property demek.
        self.komisyon = komisyon


    def hesapBilgileri(self):
        return f"\n\nHesap bilgileri:\nİsim   :{self.isim}\nNumara :{self.numara}\nBakiye :{self.__bakiye}"


    def paraCek(self, miktar):
        if self.__bakiye <= (miktar + self.komisyon):
            print(f"\n\nBakiyeniz yeterli değil...\n\
                  Bakiyeniz:{self.__bakiye}\
                  Komisyon :{self.komisyon}")
        else:
            self.__bakiye -= (miktar + self.komisyon)
            print(f"\n\nPARA ÇEKME:\n\
Yeni Bakiye   :{self.__bakiye}\n\
Çekilen       :{miktar}\n\
Komisyon      :{self.komisyon}")


    def paraYatir(self, miktar):
        self.__bakiye += (miktar - self.komisyon)
        print(f"\n\nPARA YATIRMA:\n\
Yeni Bakiye :{self.__bakiye}\n\
Yatırılan   :{miktar}\n\
Komisyon    :{self.komisyon}")




hesap1 = Hesap("Kaan Koç",584782,1000)
print(hesap1.hesapBilgileri())
# hesap1.paraCek(300)
# hesap1.paraYatir(500)
hesap1.paraYatir(100)
hesap1.paraCek(50)


hesap2 = Hesap("Emir HAN", 585478, 1000, 0)
hesap2.paraYatir(100)
hesap2.paraCek(50)