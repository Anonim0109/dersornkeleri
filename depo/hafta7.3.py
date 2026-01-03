# arbitary arguments ** ile dictionary olar
def bilgiler(**ogrenci):
    print("Gelen ogrenci bilgisi:",ogrenci)
    print("Gelen ogrenci bilgisinin tipi:",type(ogrenci))  
    for a,b in ogrenci.items():
        print(a,"bilgisinin değeri:",b)


bilgiler(adi="Efekan",numara="458")