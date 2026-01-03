import os
liste = os.listdir()


for a in liste:
    print("dosya" if os.path.isfile(a) else "klasör",end="")
    print("\t",a)


dosyaSayisi = 0
for a in liste:
    if os.path.isfile(a): dosyaSayisi +=1


print(len(os.listdir()),"adet dosya ve klasör var.")
print(dosyaSayisi,"adet dosya,",len(os.listdir())-dosyaSayisi,"adet klasör var.")