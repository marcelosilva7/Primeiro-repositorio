t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
for c in range(1, 21):
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
print('FIM', end='')