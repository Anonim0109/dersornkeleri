def topla(*sayi):
    print(sayi)
    print(type(sayi))
    toplam = 0
    for a in sayi:
        toplam += a
    print(toplam)

topla(1,2)