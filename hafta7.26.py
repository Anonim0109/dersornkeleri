# Miras alma
class Ilan():
    def __init__(aa,num=0,bas="---",ack="Girilmemiş"):
        aa.no = num
        aa.baslik = bas
        aa.aciklama = ack
   
    def bilgiVer(aa): # metod, davranış
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}"


class EvIlani(Ilan):
    def __init__(aa,num=0,bas="---",ack="Girilmemiş",m2=0):
        super().__init__(num, bas, ack)
        aa.metrek = m2


    def bilgiVer(aa): # metod, davranış
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}, Büyüklük: {aa.metrek}m2"


ilan1 = Ilan(857496,"Bayandan temiz araç","65Kmde garantisi henüz bitmemiş...")
ilan2 = Ilan(965214,"Sahibinden 3+2 daire.","Metroya, markete yakın...")
print(ilan1.bilgiVer())
print(ilan2.bilgiVer())


ilan3 = EvIlani()
print(ilan3.bilgiVer())


ilan4 = EvIlani(452147,"Metro yakını 2+1 eşyalı d.","Metroya çok yakın, memura...",150)
print(ilan4.bilgiVer())