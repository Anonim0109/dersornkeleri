# yield ile fonksiyondan sıra ile değer alma
def fonksiyon1():
    bos_koltuklar = [5,6,7,8,9,10,11,12,21,22,23,13,14,15,16]
    yield bos_koltuklar[0]
    yield bos_koltuklar[1]
    yield bos_koltuklar[2]


x = fonksiyon1()


print(next(x))
print(next(x))
print(next(x))
