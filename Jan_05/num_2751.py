# 2751번

# 코드 작성
N = int(input())
lst = []
for i in range(N):
    n = int(input())
    lst.append(n)
lst.sort()
for i in range(N):
    print(lst[i])

# 코드 시간 초과
# input() 대신 sys.stdin.readline()을 사용해야 함

import sys
N = int(input())
lst = [0]*N
for i in range(N):
    lst[i] = int(sys.stdin.readline())
lst.sort()
for i in range(N):
    print(lst[i])
