a, b = input().split()
a = [a[x:x+1] for x in range(0, len(a), 1)]
b = [b[x:x+1] for x in range(0, len(b), 1)]
bull = 0
cow = 0
s = -1
for i in a:
    s = s + 1
    if i == b[s]:
        bull = bull + 1

for i in range(0, 4):
    if a[0] == b[i] and i != 0:
        cow += 1
    if a[1] == b[i] and i != 1:
        cow += 1
    if a[2] == b[i] and i != 2:
        cow += 1
    if a[3] == b[i] and i != 3:
        cow += 1
print(bull, cow)
