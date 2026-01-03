def anamenu():
    print("╔═════════════════════╗")
    print("║     Pratik Eğlence  ║") 
    print("╠═════════════════════╣")
    print("║  1-Hesaplamalar     ║")
    print("║  2-çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  4-Sohbet           ║")
    print("║  5-Test             ║")
    print("║  6-Belge belirleme  ║")
    print("║  7-Çarpım Tablosu   ║")
    print("║  8-Çıkış            ║")
    print("║                     ║")
    print("║                     ║")
    print("║       Seçin?        ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim =="1":
        import moduller.hesapmakinesi
        moduller.hesapmakinesi.hesapmenu()
    if secim =="2":
        import moduller.cizimler
        moduller.cizimler.cizimmenu()
    if secim =="3":
        import moduller.oyunlar
        moduller.oyunlar.oyunmenu()
    if secim =="4":
        import moduller.sohbet
        moduller.sohbet.sohbetmenu()
    if secim =="5":
        import moduller.test
        moduller.test.testmenu()
    if secim =="6":
        import moduller.belgebelirleme
        moduller.belgebelirleme.belgemenu()
    if secim =="7":
        import moduller.carpımtablosu
        moduller.carpımtablosu.tablomanu()
        
    if secim =="8": exit()
    anamenu()
        
anamenu()
