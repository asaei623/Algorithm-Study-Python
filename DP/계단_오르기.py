#오답노트 : 인덱스 에러 주의하기! d 뿐만 아니라 이번에는 s 배열의 인덱스도 주의
def dp(n, s):
    # 1. 테이블 정의하기
    d = [[None] * 3 for _ in range(n + 2)]
    
    # 2. 점화식 찾기
    # d[k][1] = max(d[k-2][1], d[k-2][2]) + s[k]
    # d[k][2] = d[k-1][1] + s[k]
    
    # 3. 초기값 정하기
    d[1][1] = s[1]
    d[1][2] = 0
    d[2][1] = s[2]
    d[2][2] = s[1] + s[2]
    
    if n >= 3:
        for i in range(3, n+1):
            d[i][1] = max(d[i-2][1], d[i-2][2]) + s[i]
            d[i][2] = d[i-1][1] + s[i]
        
    return max(d[n][1], d[n][2])

# 입력
n = int(input())
s = [0] * (n + 2)
for i in range(1, n+1):
    s[i] = (int(input()))

# 출력
print(dp(n, s))
