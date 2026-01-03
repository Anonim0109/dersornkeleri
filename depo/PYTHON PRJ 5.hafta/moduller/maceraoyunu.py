import time

def yavas_yaz(metin, hiz=0.03):
    for karakter in metin:
        print(karakter, end="", flush=True)
        time.sleep(hiz)
    print()

def secim_al(secenekler):
    while True:
        cevap = input("> Seçimin (1/2): ")
        if cevap in secenekler:
            return cevap
        else:
            print("Sadece 1 veya 2 yaz aşkımm :)")

yavas_yaz("🌙 Gizemli Ormana Hoş Geldin…")
yavas_yaz("Gece serin. Uzakta bir fısıltı duyuyorsun...")

yavas_yaz("\n1) Fısıltının geldiği yere git")
yavas_yaz("2) Ormanda yoluna devam et")

secim1 = secim_al(['1','2'])

if secim1 == '1':
    yavas_yaz("\n🌫️ Fısıltıya yaklaştığında bir ruh beliriyor...")
    yavas_yaz("Ruh sana bakıp gülümsüyor.")
    yavas_yaz("\n1) Ruhla konuş")
    yavas_yaz("2) Kaç")

    secim2 = secim_al(['1','2'])

    if secim2 == '1':
        yavas_yaz("\n👻 Ruh: 'Korkma, sana yardım etmeye geldim.'")
        yavas_yaz("Bir ışık beliriyor ve eline sihirli bir taş veriyor.")
        yavas_yaz("\n1) Taşı kabul et")
        yavas_yaz("2) Teşekkür edip reddet")

        secim3 = secim_al(['1','2'])
        if secim3 == '1':
            yavas_yaz("\n💎 Taşı aldığın anda güç bedenine doluyor!")
            yavas_yaz("Süper güçlerin oldu! Oyun sonu: **Kahraman Sonu** ✨")
        else:
            yavas_yaz("\n🌬️ Ruh hüzünle kayboldu...")
            yavas_yaz("Karanlık ormanda yalnız kaldın. Oyun sonu: **Yalnız Gezgin** 🖤")

    else:
        yavas_yaz("\n🏃 Kaçarken ayağın takıldı ve düştün!")
        yavas_yaz("Orman seni kabul etmedi... Oyun sonu: **Korkak Kaçış** 💀")

else:
    yavas_yaz("\n🌲 Ormanda ilerlerken bir sandık buluyorsun.")
    yavas_yaz("Sandığın üstünde eski bir yazı var.")
    yavas_yaz("\n1) Sandığı aç")
    yavas_yaz("2) Uzaklaş")

    secim2 = secim_al(['1','2'])

    if secim2 == '1':
        yavas_yaz("\n🎁 Sandığı açtığında içinden altın taşıyor!")
        yavas_yaz("Bir ömür zengin oldun! Oyun sonu: **Hazine Sonu** 💰")
    else:
        yavas_yaz("\n🚶 Sessizce uzaklaştın…")
        yavas_yaz("Belki de kaderindeki hazineyi kaçırdın. Oyun sonu: **Sıradan Son** 🌑")
