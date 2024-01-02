# 2839번

# 문제 해석
# 설탕을 정확하게 N킬로그램을 배달해야 함. 봉지는 3킬로그램, 5킬로그램이 있음.
# 최대학 적은 봉지를 갖고 가려 함.
# 정확하게 N킬로그램을 만들 수 없으면 -1을 출력

# 코드 작성
N = int(input())
total = 0
while N >= 0:
    if N % 5 == 0:
        total += N // 5
        print(total)
        break
    N -= 3
    total += 1
else:
    print(-1)
