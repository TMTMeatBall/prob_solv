# a = input().upper()
# aa=list(set(a))
# cnt = []
# for i in a:
#     count = a.count(i)
#     cnt.append(count)
#
# if cnt.count(max(cnt)) >= 2:
#     print('?')
# else:
#     max_idx = cnt.index(max(cnt))
#     print(aa[max_idx])

# 제일 큰거 뽑고, 큰게 뭔지

# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
#
# cnt_list = []
# for x in unique_words:
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append
#
# if cnt_list.count(max(cnt_list)) > 1:  # count 숫자 최대값이 중복되면
#     print('?')
# else:
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])
#
words = input().upper()
words_set = list(set(words))
cnt_list=[]
for i in words_set:
    cnt = words.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_idx = cnt_list.index(max(cnt_list))
    print(words_set[max_idx])

#  1. set으로 감싸면 중복을 모두 제거할 수 있다.
#  2. 그 set을 리스트로 감싸면 순회가능하게 만들 수 있다. set은 순회불가(반복불가)

