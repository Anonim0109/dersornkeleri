print("╔═════════════════════╗")
print("║       Çizim         ║") 
print("╠═════════════════════╣")
print("║  1- Kare            ║")
print("║  2- Üçgen           ║")
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
    import moduller.kare
    moduller.kare.karemenu()
if secim =="2":
    import moduller.ucgen 
    moduller.ucgen.ucgenmenu()
    
cizimmenu()
