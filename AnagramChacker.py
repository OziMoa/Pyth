from collections import Counter as ct

v1 = input("ilk kelimeyi giriniz")
v2 = input("ikinci kelimeyi girin")

def is_anagram (s1, s2):
    if len(s1) != len(s2):
        print("bunlar eşit değil")
        return False
    return ct(s1) == ct(s2)

def is_anag(v1, v2):

    if len(v1) != len(v2):
        print("kelime uzunlukları bile aynı değil dalga mı geçiyorsun")
        return False

    freq1 = {}
    freq2 = {}

    for chr in v1:
        if chr in freq1:
            freq1[chr] += 1
        else:
            freq1[chr] = 1

    for chr in v2:
        if chr in freq2:
            freq2[chr] += 1
        else:
            freq2[chr] = 1
    print(freq1)
    print(freq2)


    for kw in freq1:
        if kw not in freq2 or freq1[kw] != freq2[kw]:
            print(" kullandığınız kelimeler anagram değil")
            return False
    return True

print(f"seçtiğiniz kelimeler birer anagram: {is_anagram(v1, v2)}")
print(f"seçtiğiniz kelimeler birer anagram: {is_anag(v1, v2)}")
