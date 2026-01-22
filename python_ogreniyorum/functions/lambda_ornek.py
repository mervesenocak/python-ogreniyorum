# TL'yi dolara çeviren lambda fonksiyonu
# NOT: Kur sabit alınmıştır, gerçek zamanlı veri değildir.

dolar = lambda tl: tl / 27.5

# Kullanıcıdan TL miktarı alınır
tl = float(input("TL miktarını giriniz: "))

# Dönüştürülmüş dolar miktarı ekrana yazdırılır
print("Dolar miktarı:", dolar(tl))

