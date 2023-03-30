
# dfs 방식이라면
# 방문했는지 아닌지 체크하고, 방문하지 않았으면 전부 방문하면서
# 어레이 인덱스에 맞춘 부분집합 합이 맞으면 정답 카운트에 반환, 아니라면 패스
def dfs(i,N,sum):
    #기저 조건(의 끝에는 꼭 리턴해서 아래의 메인로직이 실행되지 않게 한다)
    if i == N:

        #부분집합 합 로직
        for j in range(N):
            if vis[j] == 1:
                sum += A[j]

        if sum == 10:
            for j in range(N):
                if vis[j] == 1:
                    print(A[j])
        return
    #가지치기
    if sum > 10:
        return

    #메인로직 (해당 i인덱스 요소가 부분집합에 포함되는지)
    vis[i] = 0
    dfs(i+1,N,sum)
    vis[i] = 1
    dfs(i+1,N,sum + A[i])


A = [1,2,3,4,5,6,7,8,9,10]
N = 10
vis = [0] * N

dfs(0,10,10)