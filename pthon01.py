import random
sifre = ""
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("şifre uznunluğu girermisiniz?"))
for i in range(uzunluk):
    selected = random.choice(x)
    sifre += selected
print(sifre)


