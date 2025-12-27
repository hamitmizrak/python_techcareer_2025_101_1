##########################################################################################
#### Date ###########################################################################
# Ctrl + Shift+ Alt + L
# Shift+F10 (Çalıştırma)
from datetime import datetime

# Şimdiki zaman bilgisi
current_time=datetime.now()
print(f"Şimdiki Zaman: {current_time} ")

# Formatter
formatter_year_long= current_time.strftime("%Y-%m-%d")
print(f"Güncel Format Tarih: {formatter_year_long}")

# year kısaltması
formatter_year_short= current_time.strftime("%y")
print(f"Güncel Format Tarih: {formatter_year_short}")