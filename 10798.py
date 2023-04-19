words = []
length = []
for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

    # print(words)
    # print(length)
result = ''

for i in range(max(length)): #0~5 max(length)=6
    for j in range(5):
        if i < length[j]: #64566
# 각 줄에서의 가로길이와 비교해서 작을 떄에만,
            result += words[j][i]
print(result)

# for j in range(max(length)):
#     for i in range(5):
#         if j < length[i]:
#             result += words[i][j]

