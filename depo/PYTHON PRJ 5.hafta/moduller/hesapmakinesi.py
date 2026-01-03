print("╬══════════════════════════════════════════════════════════╬")
print("║                                                          ║")
print("║                                                          ║")
print("║                                                          ║")
print("║                PYTHON HESAP MAKİNESİ                     ║")
print("║                                                          ║")
print("║                       *, /, +, -                         ║")
print("║                                                          ║")
print("║                                                          ║")
print("║                                                          ║")
print("║                                                          ║")
print("║                                                          ║")             
print("║                                                          ║")
print("╬══════════════════════════════════════════════════════════╬")

ilksayı = int(input("ilk sayıyı giriniz. "))
ikincisayı = int(input("ikinci sayıyı giriniz. "))
işlem = input("""yapmak istediğiniz işlemi giriniz.
(toplama: +, çıkarma: -, bölme: /, çarpma: *)
""")

if işlem == "-":
    print("sonuç: " +str(ilksayı-ikincisayı))

if işlem == "*":
    print("sonuç: " +str(ilksayı*ikincisayı))

if işlem == "/":
    print("sonuç: " +str(ilksayı/ikincisayı))

if işlem == "+":
    print("sonuç: " +str(ilksayı+ikincisayı))
    
int(input("Bol şans!!"))

hesapmenu()
