import random

print("=== Taş Kağıt Makas ===")
secenekler = ["tas", "kagit", "makas"]

senin_secimin = input("Taş, Kağıt veya Makas seç: ").lower()
pc_secimi = random.choice(secenekler)

print("Bilgisayar:", pc_secimi)

if senin_secimin == pc_secimi:
    print("Berabere!🤔")
elif (senin_secimin == "tas" and pc_secimi == "makas") or \
     (senin_secimin == "kagit" and pc_secimi == "tas") or \
     (senin_secimin == "makas" and pc_secimi == "kagit"):
    print("Kazandın!")
else:
    print("Kaybettin!")