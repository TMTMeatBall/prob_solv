# n = int(input())
# 1과 자기 자신만을 약수로 가지는 수
# n개 만큼의 인풋을 받아야 함
# for문 돌리면서 각 i가 1~자기자신까지 나누되, 1과 자기 자신뿐이면 cnt += 1
# result = 0
# # while True:
# #     a = list(input().split())
# #     for i in range(n):
# #         prime_cnt = 0
# #         for j in range(1, int(a[i] + 1)):
# #             if a[i] % j == 0:
# #                 prime_cnt += 1
# #             if prime_cnt == 2:
# #                 result += 1
# print(result)
# n = int(input())
# numbers = list(map(int,input().split()))
# prime_count = 0
# for num in numbers:
#     if num == 1:
#         continue
#     prime = True
#     for i in range(2,int(num**0.5)+1):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         prime_count += 1
#
# print(prime_count)

n = int(input())
a = [int(x) for x in input().split()]
result = 0
for i in a:
    if i == 1:
        continue
    #     i 가 1인 경우에는 소수가 아니니까 제외,
    prime_cnt = 0
    # 소수인지 세는 단위
    for j in range(2, i + 1):
        if i % j == 0:
            # 2~i까지 돌면서 해당 수인 i를 나누는데, 나머지가 0이면 추가
            prime_cnt += 1
    if prime_cnt ==1:
        # 1제외 자기 자신만 되니까 1이면 결과값에 +1
        result += 1
print(result)
