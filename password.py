import hashlib
with open("document.txt") as tfile:
    f = tfile.read()
value = ""
n = int(input("Oluşturacağınız parolanın karakter sayısını giriniz:"))
for i in range(n):
    f = hashlib.md5(f.encode("utf-8")).hexdigest()
    value += f[7]
print("dec: ", int(value, 16))
