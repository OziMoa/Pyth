""" 
Soru listesine yerleştireceğiniz ikililer aracılığı ile küçük bir sınav oyunu oluşturulur. 


"""


import random

print("Testimize Hoş Geldin")

playing = input("Oynamak ister misin ? ").lower()

sorulistesi=[["the big bang", "1"], ["the pillow feels soft ", "2"], ["odd one out ", "3"], ["press conference", "4"],
             ["show me the money", "5"], ["time to go home", "6"], ["that was easy", "7"], ["hangman is cool","8"],
             ["zoologist", "9"], ["quadruplets", "10"], ["the sky is blue", "11"]]


soru = ("")
cevap = ("")

listele=[]

def random_select(liste):
    secilen = random.choice(liste)
    soru = secilen[0].lower
    cevap = secilen[1].lower


    return soru, cevap


print(str(soru), str(cevap))

dogru = 0
yanlis = 0
def dogru_say():
    global dogru
    dogru += 1

def yanlis_say():
    global yanlis
    yanlis += 1


def oyun(playing):
    global soru, cevap
    if playing != "evet":
        print("demek oynamak istemiyorsun. git başka yerde eğlen ")
        return False
    else:
        soru, cevap = random_select(sorulistesi)
        if soru not in listele:
            listele.append(soru)
        elif len(listele) == len(sorulistesi):
            global dogru, yanlis
            print("tüm soruları bitti tamamladınız! ")
            print(f"Doğru sayınız: {dogru}, Yanlış sayınız {yanlis}")
        else:
            soru, cevap = random_select(sorulistesi)

        print("O zaman başlayalım. :) ")
        return True

devam = oyun(playing)


while devam == True:

    listele.append(soru)

    answer = input(f" {soru} nedir? : ")

    if answer == cevap:
        print("Doğru")
        dogru_say()
        devammi = input("Yeni soruya geçmek istiyor musunuz ? ")
        if oyun(devammi) == True:
            devam = True
        else:
            devam = False

    else:
        print("Yanlış yaptın! ")
        devammi = input("yeni bir cevap vermek ister misin ? ")
        yanlis_say()
        if oyun(devammi) == True:
            devam = True
        else:
            devam = False


print(f"Doğru sayınız: {dogru}, Yanlış sayınız {yanlis}")
print(listele )
