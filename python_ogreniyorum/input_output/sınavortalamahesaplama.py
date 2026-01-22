y1 = int(input("Birinci yazılı notu: "))
y2 = int(input("İkinci yazılı notu: "))

ortalama = (y1 + y2) / 2

if ortalama >= 50:
    print("Geçtiniz. Ortalama:", ortalama)
else:
    print("Kaldınız. Ortalama:", ortalama)
# Kullanıcıdan iki yazılı notu alınır