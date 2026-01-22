# 0 ile 99 arasındaki sayılardan 7'nin katı olanları atlar

for a in range(100):
    if a % 7 == 0:
        continue  # 7'nin katıysa bu turu atla
    print(a)
