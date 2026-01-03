import logging
import os

# Log dosyasının adını tanımla
log_dosya_adi= "araba_log.txt"
log_dosya_yolu= os.path.join(os.getcwd(), log_dosya_adi)

# Eğer dosya varsa yeni bir dosya oluştur
if os.path.exists(log_dosya_yolu):
    yeni_log_dosya_adi= f"araba_log_{len(os.listdir(os.getcwd()))}.txt"
    log_dosya_yolu= os.path.join(os.getcwd(),yeni_log_dosya_adi)
    print(f"Dosya mevcut. Yeni log dosyası oluşturuldu: {yeni_log_dosya_adi}")
else:
    print(f"Log dosyası bulunamadı Yeni log dosyası oluşturulacak {log_dosya_adi}")

logging.basicConfig(
    filename=log_dosya_yolu,
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s: %(lineno)s= %(funcName)s, %(message)s, '
)


# ENUM