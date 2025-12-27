#######################################################
####### MATH ##########################################
import math
from random import randint, uniform


#######################################################
####### SABİT #########################################
print("PI: ", math.pi)
print("E: ", math.e)



#######################################################
####### KAREKÖK/ÜSLÜ/FAKTÖRİYEL #######################
print("Karekök: ", math.sqrt(16))
print("üslü: ", math.pow(2,5))
print("üslü: ", (2**5))
print("faktöriyel: ", math.factorial(5))
print("Yukarı yuvarla: ", math.ceil(4.001))
print("Aşağı yuvarla: ", math.floor(4.9))



#######################################################
####### LOGARITMIK ####################################
print("Logaritma: " , str(math.log(100)))
print("Sinüs: " , str(math.sin(math.radians(90))))
print("Kosinüs: " , str(math.cos(math.radians(90))))
print("Trigonometrik açıların radyan cevresi: " , str(math.radians(90)))
print("Trigonometrik açıların derece cevresi: " , str(math.degrees(math.pi/2)))



#######################################################
####### AGGREAGE ######################################
number_list=[1,2,3,4,5]
print("En büyük: ", max(number_list))
print("En küçük: ", min(number_list))
print("Sum: ", sum(number_list))
print("Average: ", sum(number_list)/len(number_list))


#######################################################################################
#### Sayısal İşlemler Rastgele  #######################################################
print("Rastgele Tam sayı: ",randint(1,100))
print("Rastgele Ondalık sayı: ",uniform(0,1))