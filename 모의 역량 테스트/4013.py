# SW Expert Academy 4013. [모의 SW 역량테스트] 특이한 자석

from collections import deque

T = int(input())

for t in range(1, T+1):
  K = int(input())

  gears = [deque([0, 0, 0, 0, 0, 0, 0, 0])]
  for _ in range(4):
    g = list(map(int, input().split()))
    gears.append(deque(g))
  gears.append(deque([0, 0, 0, 0, 0, 0, 0, 0]))

  rotation = [0] * 6  # 자석마다 회전 방향을 저장하는 리스트

  for _ in range(K):
    num, direction = map(int, input().split())

    rotation[num] = direction

    # 앞 쪽
    for i in range(num, 0, -1):
      if gears[i][6] != gears[i-1][2]:
        rotation[i-1] = -rotation[i]
      else:
        break

    # 뒤 쪽
    for i in range(num, 4):
      if gears[i][2] != gears[i+1][6]:
        rotation[i+1] = -rotation[i]
      else:
        break
    
    for i in range(1, 4+1):
      if rotation[i] == 1:
        gears[i].appendleft(gears[i].pop())
      elif rotation[i] == -1:
        gears[i].append(gears[i].popleft())
	
    rotation = [0] * 6  # 회전을 마치고나면 초기화를 해야 함

  answer = 0
  if gears[1][0] == 1:
    answer += 1
  if gears[2][0] == 1:
    answer += 2
  if gears[3][0] == 1:
    answer += 4
  if gears[4][0] == 1:
    answer += 8

  print("#{} {}".format(t, answer))
