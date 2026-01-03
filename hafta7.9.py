# filter belli şartı sağlayanlardan yeni dizi oluşturma
sayilar = [11,20,3,60,7,45,40]


def tekMi(xx):
    return xx%2==0
yeniDizi = list(filter(tekMi,sayilar)) # tek değer gönderirken fonksiyon parantezsiz yazılır
   
print(yeniDizi)