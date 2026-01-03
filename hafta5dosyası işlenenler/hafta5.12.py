# mevcut konumdaki dosya/dizin listesini alma
import os
# print(os.listdir())
liste = os.listdir()
print(*liste,sep="\n")