# SW Expert Academy 1983. 조교의 성적 매기기 D2

T = int(input())

for t in range(1, T+1):
  N, K = map(int, input().split())

  scores = []
  for i in range(N):
    mid, final, task = map(int, input().split())
    scores.append([i+1, mid, final, task])

  grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

  scores_sorted = sorted(scores, key=lambda x: x[1]*0.35 + x[2]*0.45 + x[3]*0.20, reverse=True)

  rank = scores_sorted.index(scores[K-1])

  answer = grades[rank // (N // 10)]

  print("#{} {}".format(t, answer))
