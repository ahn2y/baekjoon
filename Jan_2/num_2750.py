# 2750번

# 문제 해석
# 입력될 숫자의 개수 N개와 무작위의 숫자 N 개가 주어졌을 때
# 숫자 N개를 오름차순으로 출력하시오.

# 코드 작성
N = int(input())
lst = []
for i in range(N):
    n = int(input())
    lst.append(n)
lst.sort()
for i in range(N):
    print(lst[i])
