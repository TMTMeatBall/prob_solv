p, q = map(int, input().split())
divs = []
for i in range(1, p + 1):
    if p % i == 0:
        divs.append(i)
divs.sort()

if len(divs) < q:
    print(0)
else:
    print(divs[q-1])