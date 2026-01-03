class Araba:
    """
    Araba Field
    """
    marka = "marka yazılamadı"
    model = "model yazılmadı"
    yil = 0
    renk = "renk yazılmadı"

    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def calistir(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk}")


##############################################################################################
# Field'siz
araba_ornegi1 = Araba()
araba_ornegi1.calistir()


##############################################################################################
# Field'siz
araba_ornegi2 = Araba()
araba_ornegi2.renk ="Beyaz"
araba_ornegi2.yil ="2026"
araba_ornegi2.marka ="Audi"
araba_ornegi2.model ="A3"
araba_ornegi2.calistir()

