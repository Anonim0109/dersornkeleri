import datetime
def selam(s):
    print ("merhaba",s,type(s))
    def sabah():
        print("günaydın")
        print("hayırlı sabahlar")
    def ogle():
        print("iyi günler")
        print("günün iyidir umarım")
    if int(s) in range(7,13): sabah()
    if int(s) in range(13,18): ogle()
    else:
        print("iyi akşamlar")

saat = datetime.datetime.now().strftime("%H")
print(saat)
selam(saat)