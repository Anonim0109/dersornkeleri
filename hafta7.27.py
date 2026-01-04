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


    def bilgiVer(aa): # bilgiVer metodu ev ilanında farklı davranır. polimorfik  
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}, Büyüklük: {aa.metrek}m2"


class Arac(Ilan):
    def __init__(aa, num=0, bas="---", ack="Girilmemiş",marka="",motor =0):
        super().__init__(num, bas, ack)  
        aa.marka = marka    
        aa.motorh = motor    


    def bilgiVer(aa): # bilgiVer metodu ev ilanında farklı davranır. polimorfik  
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}, Markası:{aa.marka} Motor hacmi: {aa.motorh} "


class KiraklikEv(EvIlani):
    def __init__(aa, num=0, bas="---", ack="Girilmemiş", m2=0, depozit=0):
        super().__init__(num, bas, ack, m2)
        aa.depozito = depozit
   
    def bilgiVer(aa): # bilgiVer metodu ev ilanında farklı davranır. polimorfik  
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}, Büyüklük: {aa.metrek}, Depozito:{aa.depozito} "


class SatilikEv(EvIlani):
    def __init__(aa, num=0, bas="---", ack="Girilmemiş", m2=0, iskan=""):
        super().__init__(num, bas, ack, m2)
        aa.iskandurum = iskan


    def bilgiVer(aa): # bilgiVer metodu ev ilanında farklı davranır. polimorfik  
        return f"\n\n {aa.no} numaralı ilan Bilgisi:\n Başlık: {aa.baslik} Açıklama: {aa.aciklama}, Büyüklük: {aa.metrek}, İskan durumu:{aa.iskandurum} "


ilan1 = Ilan(857496,"Bayandan temiz araç","65Kmde garantisi henüz bitmemiş...")
ilan2 = Ilan(965214,"Sahibinden 3+2 daire.","Metroya, markete yakın...")
print(ilan1.bilgiVer())
print(ilan2.bilgiVer())


ilan3 = EvIlani()
print(ilan3.bilgiVer())


ilan4 = EvIlani(452147,"Metro yakını 2+1 eşyalı d.","Metroya çok yakın, memura...",150)
print(ilan4.bilgiVer())


ilan5 = SatilikEv(415274,"Sahibinden acil satılık", "Sahibinden kelepir daire", 120, "iskanı var")
ilan6 = KiraklikEv(968552,"Ucuz kiralık", "xxx",110,20000)
ilan7 = Arac(635248,"Temiz BMW 3.20","Bakımları yeni yapıldı...","BMW",3.20)


print(ilan7.bilgiVer())
