a = 1
while a <= 10:
    print(a)
    a += 1

b = 100
while b >= 10:
    print(b)
    if b == 10:
        break
    b -= 1

c = 1
while c <= 50:
    if c % 2 == 0:
        print(c)
    c += 1
    
d = 1
while d <= 10:
    if d % 2 == 0:
        print(d)
        break
    d += 1