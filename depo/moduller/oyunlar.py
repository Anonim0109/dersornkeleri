def oyunmenu():
    print("╔═════════════════════╗")
    print("║     OYUNLAR         ║")
    print("╠═════════════════════╣")
    print("║  1-taş kağıt makas  ║")
    print("║  2-macera oyunu     ║")
    print("║  3-                 ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-                 ║")
    print("║  7-                 ║")
    print("║  8-                 ║")
    print("║  9-                 ║")
    print("║ 10-                 ║")
    print("║ 11-                 ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
secim = input() 
if secim =="1":
    import oyunlar.tasmakas
    oyunlar.tasmakas.oyunmenu()
if secim =="2":
    import oyunlar.macera
    oyunlar.macera.oyunmenu()
input()

    

