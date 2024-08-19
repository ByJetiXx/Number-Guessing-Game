import random

sayi= random.randint(1,100)
tahmin = -1

while tahmin != sayi:
    tahmin = int(input("Bir sayı tahmin ediniz: "))
    if tahmin<sayi:
        print("Daha büyük bir sayı tahmin ediniz.")
    elif tahmin>sayi:
        print("Daha küçük bir sayı tahmin ediniz.")
    else:
        print("Tebrikler! Sayıyı doğru tahmin ettiniz.")