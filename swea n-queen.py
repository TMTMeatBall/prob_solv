# 같은 행,같은 열,대각선에 놓이면 안된다.
# (1,1)을 택헀다면, (1,i),(i,1),(i,i)를 전부 가지치기 한다.

def promising(i, j):
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i+di, j+dj
        while 0<=ni<N and 0<=nj<N:
            if arr[ni][nj]: #다른 퀸이 해당 위치에 존재함
                return 0
            ni, nj = ni+di, nj+dj #끝까지 나아갈 수 있게 설정하는 법.while에
            # 중지 조건 달고 재귀적으로 호출함
    return 1

def f(i, N):
    global cnt
    if i == N:  # 모든 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            if promising(i, j):
                arr[i][j] = 1
                f(i + 1, N)
                arr[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list([0] * N for _ in range(N))  # N*N 이차원배열
    cnt = 0
    f(0, N)
    print(f'#{tc} {cnt}')
# N이 주어진 순간, N*N의 체스판이 생긴다.
# 재귀적으로 콜하되, 가지치기를 할 것.
# 기저조건? [마지막 행 8에 닿았을 떄, 퀸을 더 놓을 수 없을 때]
# 체크할 때에 모든 방향을 생각할 필요는 없다.
# 8방 탐색 + 전체거리 하는 느낌으로
#대각선 처리의 형태에 따라 여러 가지 풀이가 나오는 Nqueen