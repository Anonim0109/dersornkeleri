# try ile hataları kontrol edebiliriz.
try:
    a = "0"
    b = 5


    # print("Sonuç:",b/0) # sıfıra bölme hatası / ZeroDivisionError
    print("Sonuç:",b/"a") # stringe bölme hatası / TypeError


except ZeroDivisionError:
    print("Sayı sıfıra bölünemez")


except TypeError:
    print("İşlemde tip yanlış.")


except Exception as aa:
    print("Hata oluştu, Kodu:",aa)
