txt = "Python"
ad = ""
for f in txt:
    if f != "h":
        ad += f
print(ad)
a = 1
while a <= 50:
    if a % 2 != 0:
        a += 1
        continue
    print(a)
    a += 1

b = 1
ad = None

while b <= 10:
    if b % 2 != 0:
        b += 1
        continue
    ad = b
    b += 1

print(ad)