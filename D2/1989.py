# SW Expert Academy 1989. 초심자의 회문 검사 D2

T = int(input())

for t in range(1, T+1):
  text = input()
  text_r = text[::-1]

  if text == text_r:
    answer = 1
  else:
    answer = 0

  print("#{} {}".format(t, answer))
