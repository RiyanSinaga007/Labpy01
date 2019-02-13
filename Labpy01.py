bil1 = int(input("Masukkan bilangan pertama = "))
bil2 = int(input("Masukkan bilangan kedua   = "))
bil3 = int(input("Masukkan bilangan ketiga  = "))

if  bil2 < bil1 > bil3:
    print("Bilangan terbesar = ",bil1)
elif bil1 < bil2 > bil3:
    print("Bilangan terbesar = ",bil2)
else:
    print("Bilangan terbesar = ",bil3)