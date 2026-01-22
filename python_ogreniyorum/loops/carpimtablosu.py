# 1'den 10'a kadar çarpım tablosunu yazdıran program

for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a} * {b} = {a * b}")
    print()  # Her sayı grubu arasına boş satır ekler
