def dp(n):
    # 1. 테이블 정의하기
    d = [0] * (n+1)
    # 2. 점화식 정의하기; d[k] = min(d[k/2], d[k/3], d[k-1]) + 1
    # 3. 초기값 정의하기; d[1] = 0
    # 4. 테이블 채우기
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)

    return d[n]
    


# 입력
n = int(input())

# 출력
print(dp(n))
