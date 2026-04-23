# SW Expert Academy 2001. 파리 퇴치 D2

T = int(input())

for t in range(1, T+1):
  N, M = map(int, input().split())
  
  graph = []
  for _ in range(N):
    graph.append(list(map(int, input().split())))

  answer = 0
  for i in range(N-M+1):
    for j in range(N-M+1):
      total = 0
      for r in range(M):
        for c in range(M):
          total += graph[i+r][j+c]

      answer = max(answer, total)

  print("#{} {}".format(t, answer))
