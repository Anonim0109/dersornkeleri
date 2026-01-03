# normal fonksiyon
def topla1(aa,bb):
    return aa+bb


print("Toplama1:",topla1(5,4))


# args ile istenilen kadar parametre yazılabilir.
def topla2(*cc): # *cc args yani argumanlar ya da parametreler demek
    # print(cc, type(cc))
    toplam = 0
    for a in cc:
        toplam +=a
    return toplam


print("Toplama2:",topla2(5,4,7,1))