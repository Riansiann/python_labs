word = input('in: ')
for i in range(len(word)):
    if word[i].isupper():
        fr = i
    if word[i].isdigit():
        sc = i + 1
        break 
step = sc - fr
ans = ''
for i in range(fr, len(word), step):
    ans += word[i]
print('out:', ans)

