# pylint: disable=C0114
""" """

# Python dinamik türlü Yüksek seviyeli interpreter bir dildir.
# Değişken türleri genel kurallar (Common Rules)
# değişken isimlendirmelerde: _(under score)
# snake_case

################################################################################
##### NUMBER (SAYILAR) #########################################################
# Number (Type ==> int)
number1 = 10  # Pozitif bir sayıdır
number2 = -10  # Negatif bir sayıdır
PI_NUMBER = 3.14159
print(f"number1:  {number1}, number2:  {number2} PI_NUMBER {PI_NUMBER}")
print(type(number1)) # type

################################################################################
##### STRING (DİZGİ) ###########################################################
# (Type == > str)
# Kelimeler
string1 = "Merhabalar Güzel insanlar-1"
string2 = "Merhabalar Güzel insanlar-2"
print(f"string1:  {string1}, string2:  {string2}")
print(type(string1)) # string1

################################################################################
##### BOOLEAN (TRUE/FALSE) #####################################################
# Boolean (True, False)
# (Type == > bool)
is_login = True
print(f"giriş yapıldı mı ?:  {is_login}")
print(type(is_login)) # string1

################################################################################
##### VARIABLE  ################################################################
number3,number4,number5=3,4,5
# number3=3
# number4=4
# number5=5

################################################################################
##### CONST  ################################################################
DATA_CONNECTION = 255