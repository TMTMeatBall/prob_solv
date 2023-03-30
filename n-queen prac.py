dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]


nx = x + dx[i]
while 0<=nx<N and 0<=ny<N:

# for i in range(8): #이동거리를 준다면 이렇게도 가능하지만,거리를 제공하지 않음
#     nx = x + dx[i]*distance
#     ny = y + dy[i]*distance
#     if nx>N or nx<0 or ny>N or ny<0:
#         flag = 1
#         break
