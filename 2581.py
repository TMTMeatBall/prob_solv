a = int(input())
b = int(input())
if a > b:
    a, b = b, a
cnt = []
for i in range(a, b + 1):
    prime_cnt = 0
    for j in range(2, i + 1):
        if i % j == 0:
            prime_cnt += 1
            if prime_cnt >=2:
                break
    if prime_cnt == 1 and i != 1:
        cnt.append(i)
if len(cnt) > 0:
    print(sum(cnt),min(cnt),sep='\n')
else:
    print(-1)

