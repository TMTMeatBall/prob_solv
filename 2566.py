arr = [list(map(int,input().split())) for _ in range(9)]
max=0
a,b = 0,0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]

for i in range(9):
    for j in range(9):
        if arr[i][j] == max:
            a,b = i,j

print(max)
print(a+1,b+1)