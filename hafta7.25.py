# Sınıf metodu oluşturma
class Ilan():
    def __init__(self,bb,aa,cc):
        self.no = bb
        self.baslik = aa
        self.aciklama = cc
   
    def bilgiVer(self):
        return f"\n\n {self.no} numaralı ilan Bilgisi:\n Başlık: {self.baslik} Açıklama: {self.aciklama}"


ilan1 = Ilan(857496,"Bayandan temiz araç","65Kmde garantisi henüz bitmemiş...")
ilan2 = Ilan(965214,"Sahibinden 3+2 daire.","Metroya, markete yakın...")


# print("\n\n",ilan1.no,"numaralı ilan Bilgisi:\n Başlık:", ilan1.baslik, "Açıklama:", ilan1.aciklama)
# print("\n\n",ilan2.no,"numaralı ilan Bilgisi:\n Başlık:", ilan2.baslik, "Açıklama:", ilan2.aciklama)
print(ilan1.bilgiVer())
print(ilan2.bilgiVer())