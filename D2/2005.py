# SW Expert Academy 2005. 파스칼의 삼각형 D2

T = int(input())

for t in range(1, T+1):
  N = int(input())

  pascal = [[0] * N for _ in range(N)]

  for idx in range(N):
    pascal[idx][0] = 1

  for i in range(1, N):
    for j in range(1, N):
      pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
  
  print("#{}".format(t))
  for i in range(N):
    answer = ''
    for j in range(N):
      if pascal[i][j] != 0:
        answer += str(pascal[i][j]) + ' '
    
    print(answer)
