# N*N의 지역
# 대각선으로만 움직일 것.
# 돌아와야 함.
# 같은 숫자가 경로에 있어서는 안됨
# cnt는 4가 최소다
# 왔던 길을 되돌아가선 안된다.
# 투어가 불가능한 케이스라면, -1을 결과반환한다.
# 지금 생각하고 있는 건, arr의 좌표를 싹 도는데, 일단 겉 부분은 못 써먹을 것이므로 가지치기로 날리고
# 나머지 좌표들 경우마다 대각선 사방탐색 하는데,

# 기저조건/가지치기/메인로직

# 1.대각선 사각형 구현
# 2.2




# T = int(input())
# for tc in range(1, T + 1):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
visited = [[0]*N for _ in range(N)]