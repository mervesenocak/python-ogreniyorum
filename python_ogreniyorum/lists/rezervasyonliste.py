# Rezervasyonu olan kişilerin listesi
liste = ['merve', 'ali', 'ayşe']

# Kullanıcıdan isim alınır
isim = input("İsim giriniz: ")

# İsim listede mi kontrol edilir
if isim in liste:
    print("Rezervasyonunuz var, hoş geldiniz", isim)
else:
    print("Rezervasyonunuz bulunmamaktadır.")
