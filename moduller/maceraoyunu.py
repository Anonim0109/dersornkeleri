print("=== MACERA OYUNU ===")
print("Ormanda tek başına yürüyorsun ve karşına iki yol çıkıyor.")

print("1) Sol patikadan git")
print("2) Sağ patikadan git")

secim1 = input("Hangi yolu seçiyorsun? (1/2): ")

if secim1 == "1":
    print("\nSol yolu seçtin. Sessiz bir göl kenarına geldin.")
    print("Bir ses duyuyorsun. Suya mı bakacaksın yoksa geri mi döneceksin?")
    print("1) Suya bak")
    print("2) Geri dön")

    secim2 = input("Seçimin (1/2): ")

    if secim2 == "1":
        print("\nSuyun içinde parlayan bir sandık buldun!")
        print("Sandığı açtın ve altın buldun! Oyunu kazandın! 🎉")
    else:
        print("\nGeri dönerken yoldan kayıp köye ulaştın.")
        print("Macera bitti, ama en azından güvendesin. 🙂")

elif secim1 == "2":
    print("\nSağ yolu seçtin. Bir mağara buldun.")
    print("Mağaranın içi karanlık ama içeriden ışık geliyor.")
    print("1) Mağaraya gir")
    print("2) Kaç")

    secim2 = input("Seçimin (1/2): ")

    if secim2 == "1":
        print("\nMağaraya girdin... Bir ejderha uyuyor!")
        print("1) Sessizce geçmeye çalış")
        print("2) Ejderhaya saldır")

        secim3 = input("Seçimin (1/2): ")

        if secim3 == "1":
            print("\nSessizce geçtin ve arka tarafta hazine buldun! 🎉")
        else:
            print("\nEjderha uyandı ve seni kovaladı! Oyunu kaybettin. 😅")
    else:
        print("\nKoştun ve ormandan çıktın. Macera kısa sürdü ama hayattasın. 🙂")

else:
    print("\nSadece 1 veya 2 yazman gerekiyordu. Macera başlamadan bitti! 😅")
