print("╔═════════════════════╗")
print("║     OYUNLAR         ║") 
print("╠═════════════════════╣")
print("║  1-Macera oyunu     ║")
print("║  2-Taş kağıt makas  ║")
print("║  3-                 ║")
print("║  4-                 ║")
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
    import moduller.maceraoyunu
    moduller.maceraoyunu.oyunmenu()
if secim =="2":
    import moduller.taskagıtmakas
    moduller.taskagıtmakas.taskagıtmakasmenu()
    
