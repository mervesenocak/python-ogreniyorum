# Kullanıcı 0 girene kadar sayı alır ve karesini hesaplar
while True:
    m = int(input("Bir sayı giriniz (çıkmak için 0): "))

    if m == 0:
        break

    print("Karesi:", m * m)

    