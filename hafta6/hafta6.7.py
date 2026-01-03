# arbitary arguments
def bilgiler(**ogrenci):
    # print(ogrenci)
    # print(type(ogrenci))  
    for a,b in ogrenci.items():
        print(a,"bilgisinin değeri:",b)

bilgiler(adi="Efekan",numara="458")