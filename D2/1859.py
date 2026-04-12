# SW Expert Academy 1859. 백만 장자 프로젝트 D2

T = int(input())

for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    max_num = prices[N-1]
    answer = 0
    for i in range(N-2, -1, -1):
        if prices[i] > max_num:
            max_num = prices[i]
        else:
            answer += (max_num - prices[i])
       	
    print("#{} {}".format(t+1, answer))
