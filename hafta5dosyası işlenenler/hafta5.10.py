import os
print(os.getcwd()) # current working directory/çalışılan klasör
yol = os.getcwd().split("\\")


print("Dosya yolu",len(yol),"parçadan oluşur.")
print("Bulunduğun sürücü:",yol[0])
print("Çalıştığın klasör:",yol[len(yol)-1])
print("Bir öncek klsör  :",yol[len(yol)-2])


print("Birleşik hali    :",'\\'.join(yol[0:len(yol)-1])) # birleştir