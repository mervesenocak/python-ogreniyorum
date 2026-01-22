def selamlama():
    while True:
        isim = input("İsminizi giriniz (çıkmak için 'çıkış' yazınız): ")
        if isim == "çıkış":
            print("Çıkılıyor...")
            break
        print("Sayın", isim, "restoranımıza hoş geldiniz!")

selamlama()

#kullanıcıdan ismini alır ve selamlar, 'çıkış' yazıldığında döngüden çıkar