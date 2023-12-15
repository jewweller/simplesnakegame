import random
sp = []
a = 'qwertyuiop[]asdfghjklzxcvbnm,./1234567890QWERTYUIOP[ASDFGHJKL;LKJZXCVBNM,/.]'
for i in range(12):
    r = random.choice(a)
    sp.append(r)
print(''.join(sp))