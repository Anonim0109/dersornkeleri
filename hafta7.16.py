# re (regular expressions)
# findall   Tüm eşleşmeler listesi
# search    Ara
# split     Böl
# sub       Uyuşanları değiştir


import re
xxx = "Ahmet al renkli bir şal-aldı."


# # tüm al ifadelerinin listesi
# print(re.findall("al", xxx))


# # şal ifadesini ara
# print(re.search("şal", xxx))


# # “al” a göre böl
# print(re.split("al", xxx))


# Boşlukları zzz yap
print(re.sub(" ", "___", xxx))