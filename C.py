# Задача C. Тренировочный контест Яндекса.


import sys

inp = []
line = ' '
while line != '\n':
    line = sys.stdin.readline()
    inp.append(line)

for l in range(len(inp)):
    inp[l] = inp[l].replace('\n', '').strip()

while '' in inp:
    inp.remove('')

n_kmd = int(inp[0])
n_kom = int(inp[2])

kmd = [int(x) for x in inp[1].split()]
kmd.sort()

fff = inp[3:3 + int(inp[2])]
kom = []
for u in fff:
    for k in range(int(u.split()[1])):
        kom.append(int(u.split()[0]))
kom.sort()

results = []
for s in kmd:
    for r in range(len(kom)):
        if kom[r] >= s:
            results.append(1)
            kom[r] = 0
            break

if sum(results) == len(kmd):
    print('Yes')
else:
    print('No')
