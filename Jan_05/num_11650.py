# 11650번

# 코드 작성
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    n = list(map(int,input().split()))
    lst.append(n)
lst.sort()
for i in lst:
    print(i[0], i[1])
