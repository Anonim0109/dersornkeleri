print("Belge Hesaplama")

giris = float(input("matematik notunuzu giriniz:"))


if giris >= 85:
   print("Tebrikler takdir belgesi!!")
   
elif giris >= 70:
   print("Teşekkür belgesi")

elif giris >= 50:
   print("Geçtin")
   
else:
    print("KALDIN, eyvah durumun vahim!!")
   
input()
