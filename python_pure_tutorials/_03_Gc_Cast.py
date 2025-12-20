################################################################################
##### GC(Garbarage Collection) #################################################
"""
Python değişeknlerin bellek yönetimi otomatik yapılır.
GC: Gereksiz belek tüketimini engeller
"""
number1 = 44  # Buradaki number1=44 artık çöptür.
number1 = 23

################################################################################
##### None  ####################################################################
# None : Python'da None özel bir veri türüdür. ve boş veya tanımsız bir değeri ifade eder.
# # (Type == > NoneType)
data = None # Tanımsız veya boş anlamına geliyor.
print("Boş değer: ",data)
print(type(data))


################################################################################
##### Cast  ####################################################################
# Cast: Type casting yani değişkenlerin Tip dönüşümlerini kullanmak

# int()        : Tam sayıya çevirir
# float()      : Virgüllü sayı çevirir
# str()        : Kelime çevirir
# bool()       : Boolean çevirir

number2="44"
print(type(number2))
print((int(number2)+16))
print((float(number2)+16))








