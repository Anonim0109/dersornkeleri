# try ile hataları kontrol edebiliriz.
try:
    a = 0
    b = 5


    print("Sonuç:",b/a)


except Exception as aa:
    print("Hata oluştu, Kodu:",aa)