def alan(u, g):
    """Dikdörtgenin alanını hesaplar"""
    return u * g


def cevre(u, g):
    """Dikdörtgenin çevresini hesaplar"""
    return 2 * (u + g)


# Kullanıcıdan kenar bilgileri alınır
u = int(input("Uzun kenar: "))
g = int(input("Kısa kenar: "))

# Sonuçlar ekrana yazdırılır
print("Alan:", alan(u, g))
print("Çevre:", cevre(u, g))
