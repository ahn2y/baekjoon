# 19532번


# 코드 작성
# 변수 a, b, c, d, e, f 나누기
a,b,c,d,e,f = map(int, input().split())

# 하나씩 대입하여 결과를 찾는 방법
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i+b*j==c and d*i + e*j == f):
            print(i,j)
