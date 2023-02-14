"""
Verdiğiniz liste içersinde istediğiniz sıradaki en büyük terime ulaşmanızı sağlayacaktır. 
"""

arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]

kacinci= input("lütfen kaçıcnı en yüksek terimi aradığınızı belirtin ")


def kth_largest(arr,kacinci):
    for i in range(kacinci-1):
        arr.remove(max(arr))
    return max(arr)

def kthrew (arr, kacinci):
    tersten = len(arr) - kacinci
    sonuc = arr[tersten]
    return sonuc

print(f"en büyük {kacinci}. terim {kthrew(arr,kacinci)} dir")
