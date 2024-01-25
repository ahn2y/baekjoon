# 13241번

# 코드 작성
import sys
input = sys.stdin.readline

li = []
def gcd(n,m):
    while True:
        m = m % n
        n, m = m, n
        if n == 0:
            return m

n, m = map(int, input().split())
print(n * m // gcd(n,m))
