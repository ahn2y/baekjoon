# 14425번

# 코드 작성
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
s = []
for i in range(N):
    s.append(input())

cnt = 0
for i in range(M):
    x = input()
    if x in s:
        cnt += 1

print(cnt)
