# 10814번

# 코드 작성
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    n, m = input().split()
    lst.append([int(n),m])
lst.sort(key = lambda x:int(x[0]))
for i in lst:
    print(i[0], i[1])
