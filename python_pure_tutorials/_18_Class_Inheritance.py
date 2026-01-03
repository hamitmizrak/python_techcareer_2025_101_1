
# Genel ortak özellikler
class Araba:

    # Constructor
    def __init__(self, marka, model,yil=0, renk="Bilinmiyor"):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        print("Araba sınıfına yeni bir araba oluşturuldu.")


    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def calistir(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk} çalıştırıldı")

    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def durdur (self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk} durduruldu")

print("####### ÜST ATA #########################################################")
araba_ornegi1 = Araba("Audi","Quatro")
araba_ornegi1.calistir()
araba_ornegi1.durdur()

##############################################################################################
print("\n####### ALT ATA (OTOMATIK) #########################################################")
# Alt class
class OtomatikAraba(Araba):
    def __init__(self,marka,model,yil,renk,vites_tipi="Otomatik"):
        super().__init__(marka,model,yil,renk)
        self.vites_tipi =vites_tipi

    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def calistir(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk} çalıştırıldı")

    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def durdur(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk} vites:{self.vites_tipi}  modta çalıştırıldı")


print("####### ÜST ATA #########################################################")
#araba_ornegi2 = OtomatikAraba("Mercedes","modelX",2025,"Siyah")
araba_ornegi2 = OtomatikAraba("Mercedes","modelX",2025,"Siyah","yarı otomatik")
araba_ornegi2.calistir()
araba_ornegi2.durdur()
