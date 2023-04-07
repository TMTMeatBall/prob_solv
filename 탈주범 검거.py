# 탈주범은 시간당 1의 거리를 움직인다
# 지하 터널에 대해서 딕셔너리 처리가 가능할지도
# tunnel = {
#     '0': [],
#     '1': [[-1, 0], [0, -1], [0, 1], [1, 0]],
#     '2': [[-1, 0], [1, 0]],
#     '3': [[0, -1], [0, 1]],
#     '4': [[-1, 0], [0, 1]],
#     '5': [[1, 0], [0, 1]],
#     '6': [[0, -1], [1, 0]],
#     '7': [[0, -1], [-1, 0]],
# }
# 50개 케이스
# 가로세로 NM은 5~50
# r,c는 0~n-1, 0~m-1
# 탈출 후 1시간 뒤에 처음 시작점인 arr[r][c]에 위치
# 1~7은 구조물 타입, 0은 터널 없음을 의미
# 이동할 수 있음을 확인하는 방법. 모든 경우를 dfs하고 방문가능했던 곳이 0이 아닌 경우에, visit체크하고 visit갯수
# 세면 답이 나오지 않을까
# 시작점 x,y , 경로 갯수 tmp, 경과 시간 1
# direction in range(pipe[arr[i][j]])
# pipe[arr[ci][cj]][direction] == 1: 일 때에, 탐색을 실시하고,
# pipe[arr[ni][nj]][opposite[direction]] == 1
# 현재 내 위치의 번호를 보고, 거기에 맞춰서 이동가능한지 확인해본다.
# 받는 터널의 부품도 나와 방향이 맞아야 이동가능한데 이걸 어떻게 구현하지 tunnel
# 한쪽이 0,1 이면 반대쪽은 1,0이어야 하므로 i,j가 반대로 뒤집혀야 함
# 여러 번 세지 않기 위해서 cnt가 있는 부분에 방문체크를 실행
# direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상 좌 우 하


pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1],
        [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
opposite = [1, 0, 3, 2]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    global cnt
    queue = []
    cnt = 0

    queue.append((x, y))
    visited[x][y] = 1
    cnt += 1

    while queue:
        x, y = queue.pop(0)
        if visited[x][y] == L:
            return cnt

        # 4방향, 범위내, 반대 뒤집힌 것과 현재 파이프 이동할 위치가 맞아떨어지면,
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and \
                    pipe[arr[x][y]][direction] == 1 and pipe[arr[nx][ny]][opposite[direction]] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    # (N세로)(M가로)(R맨홀세로)(C맨홀가로)(L탈출 후 소요시간)
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)
    print(f'#{tc} {cnt}')
