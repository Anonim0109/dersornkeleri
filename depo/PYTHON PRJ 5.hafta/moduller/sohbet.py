print("🤖 Sohbet Botuna Hoş Geldin!")

isim = input("Bot: Adın ne? \nSen: ")
print(f"Bot: Memnun oldum {isim} 🙂")

while True:
    try:
        yas = int(input("\nBot: Kaç yaşındasın? \nSen: "))
        break
    except:
        print("Bot: Yaşını sayı ile yazmalısın tatlım :)")

if yas < 13:
    print("Bot: Küçüksün ama enerjin baya yüksek olmalı 😄")
elif 13 <= yas <= 16:
    print("Bot: Ergenlik dönemi… düşünceler karmaşık olabilir ama sen iyisin 😉")
elif 17 <= yas <= 20:
    print("Bot: Gençsin ve geleceğin parlak, hissettiriyorsun 🙂")
elif 21 <= yas <= 30:
    print("Bot: En aktif yaşlar! Planların ve hedeflerin olduğuna eminim 😌")
else:
    print("Bot: Olgun ve tecrübeli biri olduğun kesin 😉")
    

hobi = input(f"nBot: Peki hobilerin neler {isim} ?")

print(f"Bot: Hmm gayet iyiymiş, '{hobi}' güzel hobi gerçekten 😊")
print("Bot: Tanıştığıma memnun oldum!")
