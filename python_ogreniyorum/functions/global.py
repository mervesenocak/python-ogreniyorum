# NOT: Global değişken kullanımı önerilmez.
# Bu örnek sadece 'global' anahtar kelimesinin nasıl çalıştığını göstermek içindir.

def topla():
    global a          # a değişkeni global olarak tanımlanır
    a = 5
    b = 6
    return a + b      # a ve b toplanıp geri döndürülür


# Fonksiyon çağrılır ve sonucu ekrana yazdırılır
print("Toplam:", topla())

# a değişkeni global olduğu için fonksiyon dışında da erişilebilir
print("Global değişken a:", a)
