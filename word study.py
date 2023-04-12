a = list(set(input().upper()))
cnt = []
for i in a:
    count = a.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(a[(cnt.index(max(cnt)))])


            #제일 큰거 뽑고, 큰게 뭔지