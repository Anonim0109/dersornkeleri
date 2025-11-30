def anamenu():
    print("╔═════════════════════╗")
    print("║     ETKİN APP       ║") 
    print("╠═════════════════════╣")
    print("║  1-Hesaplamalar     ║")
    print("║  2-çizimler         ║")
    print("║  3-Oyunlar          ║")
    print("║  4-Sohbet           ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-Çıkış            ║")
    print("║                     ║")
    print("║    Seçin?           ║")
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
    if secim =="9": exit()
        
anamenu()