puan = 100

# Sorular ve doğru cevaplar
sorular = [
    ("Fransa'nın başkenti neresi? ", ["paris"]),
    ("İzmir'in plakası ne? ", ["35"]),
    ("Tüplerde ne gazı bulunur? ", ["lpg", "propan", "bütan", "propan-bütan"])
]

for soru, dogru_cevaplar in sorular:
    cevap = input(soru).strip().lower()
    
    if cevap in dogru_cevaplar:
        print("Doğru cevap!.")
    else:
        puan -= 30
        print("Yanlış cevap! -30 puan.")

    print("Güncel puan:", puan)
    print("-" * 30)

print("Oyun bitti.")
print("Final puanın:", puan)

if puan < 50:
   print("Çalışman lazım...")

input()