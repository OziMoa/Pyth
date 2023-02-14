"""
Bu kod içerisinde sayı tahmin oyununun iki çeşidi birden denemekledir. 

oyunun başlangıcında 1 ya da 2 olmak üzere oyun seçilir. 
1 numaralı oluyda bilgisayar bir sayı seçer ve siz onu bilmeye çalışırsınız.
bilgisayar sizi tahmin konusunda yönlendirecektir. 
kaçıncı tahminde oyunun sonlandığını yazacakyır 

2 numaralı oyunda siz bir sayı seçersiniz ve bilgisayar onu bilmeye çalışır.
bilgisayar seçtiği sayıyı yansıtıp yeni tahmin aralığını belirleyecektir. 
kaçıncı tahminde oyunun sonlandığını yazacakyır 


0 sizi oyundan çıkarır 

"""

import random
import time
Sayac = 0


def sayi_kontrol(sayi):
    if sayi.isdigit():
        sayi = int(sayi)
        return sayi
    else:
        print("Lütfen Bir sayı girin. ")


while True:
    print("Tahmini siz yapmak için 1'i tahmini bilgisayarın yapması için 2'yi çıkmak için 0'a basın")
    oyun = input("Oynamak istediğiniz oyunu seçin ")

    if oyun == "1":
        ustsinir = int(input("Lütfen üst sınırı belirleyin: "))
        altsinir = 0
        print("Tahmini siz yapacaksınız. ")
        bss = random.randint(altsinir, ustsinir)
        while True:
            secilensayi = input("Tahmin ettiğiniz sayıyı girin: ")
            secilensayi = sayi_kontrol(secilensayi)
            if secilensayi > ustsinir:
                print(f"üst sınırdan büyük bir sayı girdiniz lütfen {ustsinir}dan daha kücük bir sayı giriniz")
                continue

            if secilensayi == bss:
                print(f"Cevap doğru sayı {secilensayi}. {Sayac}. denemede bildiniz ")
                Sayac = 0
                break
            else:
                if secilensayi < bss:
                    print(f"Seçtiğniiz sayi küçük lütfen yeni ve {secilensayi}dan daha BÜYÜK bir tahminde bulunun")
                    Sayac += 1
                else:
                    print(f"Seçtiğniiz sayi büyük lütfen yeni ve {secilensayi}dan daha KÜÇÜK bir tahminde bulunun")
                    Sayac += 1
                    continue

    elif oyun == "2":
        ustsinir = int(input("Lütfen üst sınırı belirleyin: "))
        altsinir = 0
        print("tahmini bilgisayar yapacak. ")
        tes = int(input("Tahmin edilmesini istediğiniz sayıyı girin :"))
        while True:
            bts = random.randint(altsinir, ustsinir)
            if bts == tes:
                print(f"bilgisayar buldu sayı {bts}, {Sayac}. denemede yaptı  ")
                Sayac = 0
                break
            else:
                print("yanlış tahmin tahmin sınırı daraltılıyor")
                if bts < tes:
                    altsinir = bts
                    print(f"yeni aralık ({altsinir} - {ustsinir})")
                    time.sleep(1)
                    Sayac += 1
                else:
                    ustsinir = bts
                    print(f"yeni aralık ({altsinir} - {ustsinir})")
                    time.sleep(1)
                    Sayac += 1
                    continue
    else:
        print("oyun sonlandırılıyor iyi günler.")
        break
