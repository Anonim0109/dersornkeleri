sorular = [
    "Fransa'nın başkenti neresidir?",
    "İzmir'in plakası kaçtır?",
    "Tüplerde ne gazı bulunur?",
]
cevaplar = [
    "Paris",
    "35",
    "propan",
]


sorulanlar =[]
devam ="Evet"
puan = 0
import random
while devam.lower() in ["evet","e","evt"]:
    soruno = random.randint(0,len(sorulanlar))
    if soruno not in sorulanlar:
        sorulanlar.append(soruno)
        cevap = input(sorular[soruno])
        if cevap.lower == cevaplar[soruno]:
            puan += 100/len(sorulanlar)
            print("bildin, puanın:",puan)
           
        else:
            print("bilemedin")
            puan = 100/len(sorulanlar)
            print("bildin, puanın:",puan)
