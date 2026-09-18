n = int(input("in_1: "))
a = []
cntT = 0
cntF = 0
for i in range(n):
    value = input(f"in_{i + 2}: ")
    a.append(value)
    if a[i].split()[-1] == 'True':
        cntT += 1
    else:
        cntF += 1
print('out:', cntT, cntF)

