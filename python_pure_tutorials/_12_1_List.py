#############################################################################
#### Data Type List #########################################################
from itertools import count

# Homojen Yapı
list_data=[1,2,4,3,5,6,7,0]

# Heterojen Yapı
# list_data=[1,2,3,4,5,6,7,8,"Malatya",True,44.23]

##### Sayma ########################################################################
# Sayma
print("~~~ Sayma (ilk data) ~~~")
print(list_data.count(0))

print("~~~ ilk Data  ~~~")
# İlk Data (Pozitif indeksleme: Sıfırdan başlar)
print(f"{list_data[0]}")

##### Son Data ########################################################################
# Son Data
print("~~~ Son Data  ~~~")
print(f"{list_data[len(list_data)-1]}") # sayma: 0 başlar
# Negatif indeksleme: -1'den başlar ve tersten gider.
print(f"{list_data[-1]}")

##### Slicing ########################################################################
# Dilimleme (Slicing)
# 1,2,4,3,5,6,7,0
print("~~~ Slicing  ~~~")
print(list_data[1:4])   # [2, 3, 4]     1<=X<=4-1
print(list_data[0:4])   # [1, 2, 3, 4]  0<=X<=4-1
print(list_data[:4])    # [1, 2, 3, 4]  0<=X<=4-1
print(list_data[::3])   # Her 3 göster  0  3  6 9

##### append ########################################################################
# Yeni bir öğe ekleme
print("~~~ append  ~~~")
list_data.append(44)
print(list_data)

##### remove ########################################################################
# Öğeyi kaldırma Not: 1 başla
print("~~~ remove  ~~~")
list_data.remove(1)
print(list_data)

##### List Comprehension #######################################################
# Liste Anlama (List Comprehension):
print("~~~ List Comprehension  ~~~")
squares = [x^2 for x in range(10)]
print(squares, end=" - ")  # end ile yanyana yazmak
print()


##### İterasyon ########################################################################
# İterasyon (Döngü ile Gezinme)
print("~~~ İterasyon  ~~~")
for temp in list_data:
    print(temp)



##### in , not in  ########################################################################
# `in` ve `not in` Operatörleri:
# Bir öğenin listede olup olmadığını kontrol eder.
# 2, 4, 3, 5, 6, 7, 0, 44
print("~~~ in , not in  ~~~")
print(2 in list_data)
print(23 not in list_data)

##### nested_list ########################################################################
# İç İçe Listeler (Nested Lists):
print("~~~ nested_list  ~~~")
nested_list = [[1, 2, 3], [4, 5, 6]]
print(f"{"nested list",nested_list[0][1]}")
print(f"{"nested list",nested_list[1][1]}")


##### reverse ########################################################################
# Ters çevirme
print("~~~ reverse  ~~~")
list_data.reverse()
print(list_data)

##### sort ########################################################################
# Sıralama
print("~~~ sort  ~~~")
list_data.sort()
print(list_data)

##### reverse ########################################################################
# Ters çevirme
print("~~~ reverse  ~~~")
list_data.reverse()
print(list_data)


