# 언제 백트래킹을 사용하는가
# dfs처럼 전체를 둘러봐야 할 필요가 있을 때, 하지만 너무 경우의 수가 많을 때
# 파이썬의 경우, 재귀 콜은 최대 1천번 정도
# dfs의 핵심은 재귀 호출. 재귀 호출의 핵심은 어떤 변수가 계속 갱신될 필요가 있는가.
# 이차원 배열이 필요한가?
# n*n체스판에 n개의 퀸을 놓는다. 1개 줄에는 1개의 퀸만이 놓인다. 그러므로 이차원배열일 필요는 없다.

def nqueen(n):
    global cnt
    # 기저조건 제대로 1개의 안정된 케이스가 완성됨
    if n == N:
        cnt += 1
        return cnt

    for j in range(N):
        if visited[j] == visited_2[n + j] == visited_3[n - j] == 0:
            visited[j], visited_2[n + j], visited_3[n - j] = 1, 1, 1
            nqueen(n + 1)
            visited[j] = visited_2[n+j] = visited_3[n-j] = 0 #1개

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N  # 1개 행에 하나씩 퀸이 놓이기 때문에,  열에 퀸이 놓였는지 아닌지만 확인하면 된다.
    # 모든 줄에 퀸이 놓이면 종료. 기저 조건에 사용가능 N번째 라인에 닿으면 종료함.
    visited_2 = [0] * 2 * N
    visited_3 = [0] * 2 * N
    cnt = 0  # 답 변수로 갱신할 필요는 없고, 글로벌 변수로
    nqueen(0)
    print(f'#{tc} {cnt}')
# 기저조건, nonpromising 가지치기, 메인 로직 3단구성
# 0행에 놓는다. 열은 0~n-1로 자유
# 두 번째 퀸을 1행에 놓는다. 열은 0~n-1로 자유
# ....
# N-1번째 행에 놓는다. 열은 자유
# visited를 통해 열 관리, visited[j] == 0인 곳에만 놓는다. 행은 언제나 한 곳에 하나만 놓으니까 생각하지 않아도 된다.
# 가로 세로는 정리됨. 대각 정리
# 룩업테이블 visited_2[i+j],visited_3[i-j]
# 루프 돌면서 이차원배열 도는 방식(따로 도전해보기)
# 재귀하면서 초기화시켜야 할 변수도 있다.