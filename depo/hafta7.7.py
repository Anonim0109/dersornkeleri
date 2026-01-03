# mapsiz şekli
urunFiyatlari = [100,200,30]


def yariyaIndir(xx):
    return xx-(xx*33//100)
   #return xx//2


# yeniFiyatlar=[]
# for a in urunFiyatlari:
#     yeniFiyatlar.append(yariyaIndir(a))


# mapli şekli
yeniFiyatlar = list(map(yariyaIndir,urunFiyatlari))


print("urunFiyatlari:",urunFiyatlari)
print("yeniFiyatlar:",yeniFiyatlar)