# 11651번

# 코드 작성
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    m, n = map(int,input().split())
    lst.append([n,m])
lst.sort()
for i in lst:
    print(i[1], i[0])
