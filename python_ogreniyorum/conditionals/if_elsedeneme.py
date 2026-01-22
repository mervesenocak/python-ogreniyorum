# Kullanıcıdan iki sayı alınır
say1 = int(input("1. sayıyı giriniz: "))
say2 = int(input("2. sayıyı giriniz: "))

# Sayılar karşılaştırılır
if say1 > say2:
    print("Birinci sayı ikinci sayıdan büyüktür.")
elif say1 < say2:
    print("İkinci sayı birinci sayıdan büyüktür.")
else:
    print("İki sayı birbirine eşittir.")
# Kullanıcıdan iki sayı alır ve karşılaştırır, sonuçları yazdırır