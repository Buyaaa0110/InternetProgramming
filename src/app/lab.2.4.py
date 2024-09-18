too = [1,1,1,1,1,2,2,2,2,3,3,3,3]
a = []
for b in too:
    if b not in a:
        a.append(b)
print(a)