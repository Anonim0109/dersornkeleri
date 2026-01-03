# filter belli şartı sağlayanlardan yeni dizi oluşturma
sayilar = [11,22,3,6,7,42,43,44]


# yeniDizi = list(filter(lambda x:True,sayilar))
yeniDizi = list(filter(lambda x: x%2==0,sayilar))
   
print(yeniDizi)