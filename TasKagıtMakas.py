"""
Taş Kağıt Makas Oyunu 

seçimlerinizi Taş Kağıt ya da Makas olarak giriniz 

"""


import random

temel = {1: 'Taş', 2: 'Kağıt', 3: 'Makas'}

saybil = 0
sayins = 0


def kontrol(obj1, obj2):
    """kullanılırken seçimleri eklemeyi unutmayın 2 seçenek girilmeli
    bu fonksiyon sayesinde bilgisayarın ve bizim tahminimizin karşılaştırmasını yapacağız"""

    global sayins, saybil
    if obj1 == obj2:
        print("Eşitlik söz konusu lütfen yeni bir seçim yapın.")
        return True

    elif obj1 == 'taş':
        if obj2 == "kağıt":
            print("Bilgisayar Kazandı.")
            saybil += 1
            return True
        elif obj2 == "makas":
            print("Siz kazandınız.")
            sayins += 1
            return True

    elif obj1 == 'kağıt':
        if obj2 == "makas":
            print("Bilgisayar Kazandı.")
            saybil += 1
            return True
        elif obj2 == "taş":
            print("Siz kazandınız.")
            sayins += 1
            return True

    elif obj1 == 'makas':
        if obj2 == "taş":
            print("Bilgisayar Kazandı.")
            saybil += 1
            return True
        elif obj2 == "kağıt":
            print("Siz kazandınız.")
            sayins += 1
            return True

    else:
        print("Oyundan çıkılıyor... ")
        return False


print('Taş Kağıt Makas oyununua hoş geldiniz')

while True:
    girdi = input("Lütfen tercih seçtiğniz objeyi yaızınız: ")
    if girdi == 'ç':
        print(f"çıkış yapılıyor sonuçlar: bilgisayar ({saybil}), siz ({sayins})")
        break

    if girdi not in ["taş", "kağıt", "makas"]:
        print("Girdiniz yanlış yeniden deneyin. ")
        continue
    else:
        sec = temel[random.randint(1, 3)]
        kontrol(girdi.lower(), sec.lower())
        print(f"Siz {girdi} seçtiniz, Bilgisayar {sec} seçti bu durumda sonuclar {sayins} e karşı {saybil} \n ")
