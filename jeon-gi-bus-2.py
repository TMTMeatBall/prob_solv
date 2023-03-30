#정류장에는 충전지가 있다.
#각 충전지는 운행거리 한계가 있다.
#목적지인 종점에 도착하는데에 필요한 최소 교환횟수를 출력하는
#프로그램을 작성
#단순 dfs로 cnt세어가면서 하면?
def bus(i,cnt):
    global min_cnt
    #가지치기 조건.
    if cnt >= min_cnt:
        return
    #기저 조건
    if i >= N-1: #pop했으므로 K는 N-1만큼 갖는다
        if min_cnt >= cnt:
            min_cnt = cnt
        return
    #메인 로직
    for j in range(K[i]): #왜 이렇게 함?
        bus(i+j+1, cnt + 1) #


T = int(input())
for tc in range(1,T+1):
    K = list(map(int,input().split()))
    N = K.pop(0)
    min_cnt = 100000
    bus(0,-1) #최초로 1회 나아갈 때 정류장에서 배터리를 받는데(K[0])
    # 이 때 cnt+1되지만 실제로는 0회로 봐야 하기 때문에 -1로 시작함)
    print(f'#{tc} {min_cnt}')
#함수가 리턴해야 할 값
#dfs로 쭉쭉쭉 경우의 수를 받다가,
# 기저조건을 만날 때에 cnt와 total을 비교?
# 리스트 마지막에 0을 주고 idx가 0의 인덱스에 닿으면?
#기저조건은? 0에서 출발하는 버스가 N-1(인덱스) 에 닿았을 떄(끝까지 갔을 떄)
#버스는 인덱스 0에서 출발한다.
#def(0,