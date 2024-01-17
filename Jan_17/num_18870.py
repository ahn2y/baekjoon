import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
lt = sorted(list(set(lst)))
dic = {}
for i in range(len(lt)):
    dic[lt[i]] = i
for i in lst:
    print(dic[i], end = ' ')
