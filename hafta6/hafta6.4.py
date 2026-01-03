# Kullanıcı Adı ve Parola Kontrolü / Şifre kontrol 
# break deyimi -> döngünün içinde break çalıştırıldığı zaman döngü sona erer.
dkullanici = "adm"; dparola = "1234"
hak = 3; deneme = 0

while True:
    kullanici = input("Kullanıcı Adı:")
    parola    = input("Parola       :")

    if (kullanici == dkullanici and parola == dparola):
        print("Hoşgeldiniz", kullanici)
        break

    elif (kullanici != dkullanici and parola == dparola):
        print("Kullanıcı Adınızı yanlış girdiniz")
        deneme +=1

    elif (kullanici == dkullanici and parola != dparola):
        print("Şifreyi yanlış girdiniz")        
        deneme +=1

    else:
        print("Tekrar Deneyin")

    if deneme>=hak :
        print("3 kez yanlış giriş. Program bloke oldu.")
        break