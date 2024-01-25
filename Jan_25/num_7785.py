# 7785번

# 코드 작성
import sys
input = sys.stdin.readline

N = int(input())

coo = {}
for i in range(N):
    n, m = input().split()
    if m == "enter":
        coo[n] = 1
    else:
        del coo[n]
        
coo = sorted(coo.keys(), reverse = True)
for i in coo:
    print(i)
