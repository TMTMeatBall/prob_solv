
board = [[0]*100 for _ in range(100)]

N = int(input())
cnt = 0
for _ in range(N):
    x,y = map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            if board[i][j] == 0:
                board[i][j] += 1
                cnt += 1

print(cnt)