# Sabit kullanıcı bilgileri
KULLANICI_ADI = "admin"
PAROLA = "1234"

# Kullanıcıdan giriş bilgileri alınır
user = input("Kullanıcı adı: ")
password = input("Parola: ")

# Kullanıcı adı ve parola kontrol edilir
if user == KULLANICI_ADI and password == PAROLA:
    print("Giriş başarılı, hoş geldiniz.")
else:
    print("Giriş başarısız, tekrar deneyiniz.")
