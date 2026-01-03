# re
# findall   Tüm eşleşmeler listesi
# search    Ara
# split     Böl
# sub       Uyuşanları değiştir


import re
xxx = "Ahm854et al 5 re8547nkli bir 54 şal-658aldı."


# print(re.findall(r"\d+", xxx))  
print(re.findall(r"\d{3}", xxx))