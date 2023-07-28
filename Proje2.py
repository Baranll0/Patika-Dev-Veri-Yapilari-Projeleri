"""
        Bol ve fether yaklaşımını kullanan bir sıralama algoritması. Bu algoritma, bir diziyi yarıya böler, her iki yarısını
        ayrı ayrı sıralar ve sonra bu sıralı yanları birleştirir. İşte yukarıdaki dizinin Merge Sort algoritması ile sıralanma adımları:

        Dizi:[16,21,11,8,12,22]

        1.Adım: Diziyi yarıya bölelim: [16,21,11], [8,12,22]
        2.Adım: Her iki yarıyı da ikiye bölelim: [16],[21,11],[8],[12,22]
        3.Adım: Yine diziyi yarıya bölelim: [16],[21],[11],[8],[12],[22]
        4.Adım: Her bir çifti kendi içinde sıralayıp birleştirelim: [16],[11,21],[8],[12,22]
        5.Adım: Sıralı olan bu alt dizileri birleştirip tekrar sıralayalım:[11,16,21],[8,12,22]
        6.Adım: Son olarak, tüm alt dizileri sıralayıp birleştirelim.[8,11,12,16,21,22]
    """
def merge_sort(array):

    if len(array)<=1:
        return array
    mid=len(array)//2
    left_half=array[:mid]
    right_half=array[mid:]

    return merge(merge_sort(left_half),merge_sort(right_half))

def merge(left,right):
    merged=[]
    left_index=0
    right_index=0

    #Karşılaştırmalar ve Birleştirmeler
    while left_index<len(left)and right_index<len(right):
        if left[left_index]<right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
    #Kalan Öğeleri Ekleyelim.
    while left_index<len(left):
        merged.append((left[left_index]))
        left_index+=1
    while right_index<len(right):
        merged.append(right[right_index])
        right_index+=1
    return merged

#Test
array=[16,21,11,8,12,22]
print(merge_sort(array))

"""
Merge Sort algoritmasının zaman karmaşıklığı genel olarak O(nlogn)'dir.
Bir,hem en kötü durumda hem de en iyi durumda geçerlidir.Çünkü algoritma diziyi her seferinde ikiye böler(logaritmik zaman)
ve sonra her birini tekrar birleştirir(lineer zaman).Bu yüzden genel olarak zaman karmaşıklığı O(nlogn) olur.

Uzay Karmaşıklığı ise O(n)'dir. Çünkü algoritma, giriş dizisi boyutunda ekstra alan gerektirir. Çünkü her bir alt dizi
için yeni bir dizi oluşturur ve bu alt dizileri birleştirirken ekstra bir dizi daha kullanır.Bu da algoritmanın uzay karmaşıklığını
O(n) yapar. 
"""
