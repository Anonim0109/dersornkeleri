sayilar = [1, 2, 3, 4, 5, 6]

def cift_mi(x):
    return x % 2 == 0

sonuc = list(filter(cift_mi, sayilar))
print(sonuc)
