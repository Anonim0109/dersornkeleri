# yield ile fonksiyondan sıra ile değer alma
def fonksiyon1():
    yield "Merhaba"
    yield 51
    yield "Selam"


x = fonksiyon1()


print(next(x))
print(next(x))
print(next(x))