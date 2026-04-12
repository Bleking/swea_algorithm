# SW Expert Academy 24420. 집합 비교 D3

T = int(input())

for t in range(T):
    a_size, b_size = map(int, input().split())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A, B = set(A), set(B)
    
    if A == B:
        print('=')
    elif A < B:
        print('<')
    elif A > B:
        print('>')
    else:
        print('?')
