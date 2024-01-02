# 25305번

# 코드 작성
N, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[N-k])
