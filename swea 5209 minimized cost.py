# N종의 제품을 N곳의 공장에서 한 곳당 한 가지씩 생산하고자 함

# nn n룩 인데, 생산비가 최소가 되면된다.

# 단순 백트래?킹?문?제?
# 3개 지점을 찍는데, 찍힌 지점에서 같은 행,열에 다른 선택지가 있어서는 안된다.
# 그와 동시에 합계가 가장 적은 것을 찍어내면 될지도?

# 재귀 호출

# 가지치기
# def promising(i, j):
#     for di, dj in [[-1, 0][0, -1]]:
#         ni, nj = i + di, j + dj
#         while 0<=ni<N and 0<=nj<N:
#             if array[ni][nj]:
#                 return 0
#             ni, nj = ni+di, nj+dj
#     return 1

# 메인 로직 (#1.단순 dfs)
def fac(i, N):
    global min_cost, total
    if i == N:
        if min_cost > total:
            min_cost = total
        return

    if total >= min_cost:
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            total += array[i][j]
            fac(i+1,N) #재귀호출 잊지말기
            visited[j] = 0
            total -= array[i][j]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 10000000
    total = 0
    visited = [0] * N

    fac(0,N)

    print(f'#{tc} {min_cost}')