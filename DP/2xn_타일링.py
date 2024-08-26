def dp(n):
    # 1. 테이블 정의
    d = [0] * (n+2)

    # 2. 점화식
    # D[k] = D[k-1] + D[k-2]

    # 3. 초기값
    d[1] = 1
    d[2] = 2
    
    # 점화식
    if n >= 3:
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]

    return d[n]
    


# 입력
n = int(input())

# 출력
print(dp(n)%10007)
        
