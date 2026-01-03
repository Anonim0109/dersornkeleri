import random
import time

secenekler = ["taş", "kağıt", "makas"]

print("🪨📄✂️ Taş Kağıt Makas Oyununa Hoş Geldin!")
time.sleep(0.5)

while True:
    oyuncu = input("\nSeçimin (taş / kağıt / makas): ").lower()
    
    if oyuncu not in secenekler:
        print("Sadece 'taş', 'kağıt' veya 'makas' yaz aşkımm.")
        continue

    bilgisayar = random.choice(secenekler)

    print(f"Bilgisayar: {bilgisayar}")

    if oyuncu == bilgisayar:
        print("🤝 Berabere!")
    elif (oyuncu == "taş" and bilgisayar == "makas") or \
         (oyuncu == "kağıt" and bilgisayar == "taş") or \
         (oyuncu == "makas" and bilgisayar == "kağıt"):
        print("🎉 Kazandın aşkımm!")
    else:
        print("😢 Kaybettin...")

    tekrar = input("Tekrar oynamak ister misin? (e/h): ").lower()
    if tekrar != "e":
        print("👋 Görüşürüz aşkımm!")
        break
