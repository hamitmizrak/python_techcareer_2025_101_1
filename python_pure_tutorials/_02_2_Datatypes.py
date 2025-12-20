# pylint: disable=C0114
""" """

# Python dinamik türlü Yüksek seviyeli interpreter bir dildir.
# Değişken türleri genel kurallar (Common Rules)
# değişken isimlendirmelerde: _(under score)
# snake_case

################################################################################
##### LIST  ####################################################################
# (Type == > list)
my_list1 = [1,1,1, 2, 3, 4, "Malatya"]
my_list2 = [5, 6, 7, 8, True, "Elazığ", 14.53]
print(f"list1: {my_list1}")
print(f"list2: {my_list2}")
print(type(my_list1)) #

################################################################################
##### TUPLE ####################################################################
# Liste yapısına çok benzer bunda sadece immutable(değişmez)
# (Type == > tuple)
my_tuple = (1,1,1, 2, 3, 4, "Malatya")
print(f"my_tuple: {my_tuple}")
print(type(my_tuple)) #


################################################################################
##### SET  ####################################################################
# Set : Aynı verierlden sadece 1 tanesi gösterir(unique )
# (Type == > set)
my_set = {1,1,1, 2,2, 3, 4, "Malatya"}
print(f"my_set: {my_set}")
print(type(my_set)) #

################################################################################
##### DICTIONARY (Sözlük)#######################################################
# (Type == > dict)
person = {
    "name": "Hamit",
    "surname": "Mızrak",
    "is_login": True,
    "hes_code":1456621545
}
print(person)
print(type(person))