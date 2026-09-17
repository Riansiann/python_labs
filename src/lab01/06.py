n = int(input())
a = []
cntT = 0
cntF = 0
for i in range(n):
    a.append(input())
    if a[i].split()[-1] == 'True':
        cntT += 1
    else:
        cntF += 1
print('out:', cntT, cntF)

