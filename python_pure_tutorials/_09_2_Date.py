##########################################################################################
#### Date ###########################################################################
# Ctrl + Shift+ Alt + L
# Shift+F10 (Çalıştırma)
from datetime import datetime


# Kullancııdan Veri al
user_input= input("Tarih Giriniz: (YYYY-MM-DD): ")

# Formatter
date_object= datetime.strftime(user_input, '%Y-%m-%d')
print(f"Güncel Format Tarih: {date_object}")
