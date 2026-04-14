# SW Expert Academy 24696. 직육면체 자르기 D3

T = int(input())

for t in range(T):
  A, B, C = map(int, input().split())

  if A * B * C % 2 == 0:
    print(1)
  else:
    print(2)
