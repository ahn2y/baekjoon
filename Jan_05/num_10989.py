# 10989번

# 코드 작성
import sys
N = int(input())
lst = [0]*N
for i in range(N):
    lst[i] = int(sys.stdin.readline())
lst.sort()
for i in range(N):
    print(lst[i])

# 메모리 초과
# 계수 정렬 사용
# 카운트 할 배열을 선언하고, 정렬할 배열 요소가 몇 개가 있는지 카운트 배열 각 인덱스에 담는다
# 데이터의 크기가 한정되어 빠르게 동작해야 할 때 사용된다.

import sys
input = sys.stdin.readline
N = int(input())
lst = [0] * (10000 + 1)
for i in range(N):
    lst[int(input())] += 1
for i in range(len(lst)):
  if lst[i] != 0:
      for j in range(lst[i]):
          print(i)
