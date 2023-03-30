# 1. 2진수를 10진수로
def btod(bina):
    d = 0
    cnt = 1  # 2^0
    for i in bina[::-1]: #인덱싱 있으므로 리스트 형태로 들어가는 변수 bina
        d += cnt * i
        cnt = cnt * 2
    return d


# 2. 10진수를 3진수로  # ex) 100(10) -> 10201(3) 20(10)->'2',6->'20',2->'202'(3),0
def dtot(d):
    result = ''
    while d >= 3: #d가 3보다 크다면 계속 나눠져야 함
        result = str(d % 3) + result #3으로 나눈 나머지를 계속 결과반환함
        d = d // 3 #단, 그 때마다 나누는 d는 3으로 나눠진 몫이어야 함
    if d:
        result = str(d) + result #while문을 끝까지 돌리고 마지막 남은 나머지0,1,2를 str변환해서
        # result끝에 붙이는 것
    return result

def aa():
    for i in range(len(bina)):
        bina[i] = bina[i] ^ 1 #위치 하나 바꿔주고, 십진수로 변환 bina[i] or 1 하나 바뀔 때에 bina[i] ==1이면 0으로, 0이면 1로 한개씩 바뀔 것
        decimal = btod(bina) #이진수의 십진수 변환
        ans = dtot(decimal) #변환된 십진수를 다시 삼진수로 변환
        if len(ans) == len(tri): #원래 인풋받은 3진수와 새롭게 구한 이진수->삼진수한 삼진수의 길이 체크 (둘 다 문자열임)
            cnt = 0
            for j in range(len(tri)): #인풋 삼진수 돌면서
                if cnt >= 2: #2회 이상 다른게 확인되면,
                    break #떙
                if ans[j] != tri[j]: #다른 자릿수가 걸리면, cnt에 1씩 올린다.
                    cnt += 1
            else:
                if cnt == 1:
                    return decimal
        bina[i] = bina[i] ^ 1 #바꾼 자릿수를 원래대로 바꿔준다.
# 종료 조건
# 메인 로직

T = int(input())
for tc in range(1,T+1):
    bina = list(map(int,input()))
    tri = input()
    print(f'#{tc} {aa()}')
# a. 2진수 -> 10진수 -> 3진수 하고 비교해서 1개만 다를 경우에 값 반환
# ----
# b. 이진수를 돌면서 하나씩 바꾸는 것으로 원래 숫자의 가능성이 있는 경우를 cand 에 담고,
# 삼진수를 돌면서 0일 때에 1,2/1은 0,2/2는 0,1로 바꿔보면서 바꾼 숫자가 cand에 있는지 확인하고 있으면 return반환
# ----
# 각각 한 자리씩만 다르다.