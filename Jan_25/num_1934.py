# 1934번

# 코드 작성
import sys
input = sys.stdin.readline

N = int(input())
li = []
def gcd(n,m):
    while True:
        m = m % n
        n, m = m, n
        if n == 0:
            return m

for i in range(N):
    n, m = map(int, input().split())
    li.append(n * m // gcd(n,m))

for i in li:
    print(i)
