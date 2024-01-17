# 10815번

# 코드 작성
N = int(input())
lst = list(map(int,input().split()))
M = int(input())
lt = list(map(int,input().split()))
num = [0] * M
intersection = set(lst) & set(lt)
for i in range(M):
    if lt[i] in intersection:
        num[i] = 1
for i in num:
    print(i, end = ' ')
