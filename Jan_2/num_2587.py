# 2587번

# 코드 작성
lst = []
aver = 0
for i in range(5):
    n = int(input())
    lst.append(n)
    aver += n
lst.sort()
aver /= 5
print(int(aver))
print(lst[2])
