# 1427번

# 코드 작성
import sys
input = sys.stdin.readline
n = sorted(input().strip(), reverse = True)
for i in range(len(n)):
    print(n[i], end = '')
