def insertion_sort(array):
    """
        1. Adım: 22,28 karşılaştırılır. Zaten 22 daha küçük olduğu için değişiklik yok.[22,27,16,2,18,6]
        2. Adım: 16,27 ile karşılaştırılır. 16 Daha küçük olduğundan 27 ile yer değiştirir.
                 Ardından; 16,22 ile karşılaştırılır ve yine küçük olduğu için yer değiştirilir.[16,22,27,2,18,6]
        3.Adım:  2; 27,22 ve 16 ile karşılaştırılır. Bunlardan küçük olduğu için en başa dönecektir.[2,16,22,27,18,6]
        4.Adım:  18; 27 ile karşılaştırılır ve yer değiştirir. 22 ile karşılaştırılır yine yer değiştirir.
                 Fakat 16'dan büyük olduğu için konumunu korur.[2,16,18,22,27,6]
        5.Adım:  6;27,22 18 ve 16 ile karşılaştırılır ve yer değiştirir fakat 2 den büyük olduğundan dolayı konumunda kalır.
                  [2,6,16,18,22,27]

        Insertion Sort'un Big-O gösterimleri:
        Best Case: O(n)(Dizi zaten sıralı olduğunda)
        Average Case: O(n^2)
        Worst Case: O(n^2)(Dizi tamamen ters sıraı olduğunda)

        Tıme Complexity: 18 sayısının durumu sıralama sürecinde Average Case'e girer. Çünkü 18 sayısı dizinin ortalarında ve
        birkaç işlem sonucunda doğru konumuna yerleştirilmiştir. Bu da Average Case tanımına uygun düşmektedir.
        Aradığımız sayınn ortada olması durumu, ekleme sıralamasının genellikle ortalama zaman karmaşıklığına yol açar.
        ------------------
        Algoritmanın Zaman karmaşıklığı O(n^2)'dir. Bu, algoritmanın dizinin uzunluğu karesi ile orantılı olduğu anlamına gelir.
        Dizi sıralandıktan sonra 18 sayısı best case
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

array = [22, 27, 16, 2, 18, 6]
print(insertion_sort(array))

#-----------------
#Selection Sort
#-----------------

def selection_sort(array):
    """
        1.Adım : Dizi taranır ve en küçük eleman bulunur. Bu eleman,dizi içerisinde ilk eleman ile yer değiştirilir.
        2.Adım : İkinci elemandan itibaren dizi tekrar taranır ve en küçük eleman bulunur. Bu eleman, dizi içerisindeki
                 ikinci eleman ile yer değiştirilir.
        3.Adım : Üçüncü elemandan itibaren dizi tekrar taranır ve en küçük eleman bulunur. Bu eleman,dizi içerisindeki
                 üçüncü eleman ile yer değiştirilir.
        4.Adım : Bu işlem, dizi boyunca devam eder. Her adımda, kalan dizi içindeki en küçük eleman bulunur
                 ve dizinin o adımdaki elemanı ile yer değiştirilir.
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

array=[7,3,5,8,2,9,4,15,6]
print(selection_sort(array))
#------------------------
