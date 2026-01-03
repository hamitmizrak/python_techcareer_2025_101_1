class ArabaConstructor:

    # Constructor
    def __init__(self, marka="Bilinmiyor", model="Bilinmiyor",yil=0, renk="Bilinmiyor"):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.renk=renk
        print("Araba sınıfına yeni bir araba oluşturuldu.")


    # self: Python'da bir metot içinde o anki nesne erişmek istiyorsak
    def bilgileri_goster(self):
        print(f"Marka: {self.marka} Model: {self.model} Yıl: {self.yil} renk:{self.renk}")


    # SETTER AND GETTER
    # Marka Set, Get
    def set_marka(self,marka):
        self.marka=marka

    def get_marka(self):
        return self.marka

    # Model Set, Get
    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    # Renk Set, Get
    def set_renk(self, renk):
        self.renk = renk

    def get_renk(self):
        return self.renk


    # Yıl Set, Get
    def set_yil(self, yil):
        # Validation
        if yil>=2020:
            self.yil=yil
        else:
            print("2020 altındaki arabalar alınmıyor")

    def get_yil(self):
        return self.yil


##############################################################################################
print("################################################################")
# Field'siz
araba_ornegi1 = ArabaConstructor()
araba_ornegi1.bilgileri_goster()


##############################################################################################
print("################################################################")
araba_ornegi2=  ArabaConstructor()
araba_ornegi2.set_yil(2020)
araba_ornegi2.set_model("Corolla")
araba_ornegi2.set_renk("Gri")
araba_ornegi2.set_marka("Toyota")
araba_ornegi2.bilgileri_goster()