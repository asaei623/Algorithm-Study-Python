#오답노트 : 인덱스 에러 주의하기! d 뿐만 아니라 이번에는 s 배열의 인덱스도 주의
#오답노트 : n = 1인 경우, 인덱스 에러를 방지하기 보다 d[2]의 경우를 만들지 않기 위해 s[1]를 바로 리턴한다.
def dp(n, s):
    # 1. 테이블 정의하기
    d = [[None] * 3 for _ in range(n + 2)]
    
    # 2. 점화식 찾기
    # d[k][1] = max(d[k-2][1], d[k-2][2]) + s[k]
    # d[k][2] = d[k-1][1] + s[k]
    
    # 3. 초기값 정하기
    ### 예외처리 : n = 1일 경우 s[1]만 출력 후 종료
    if n == 1:
        return s[1]
    
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

------------------------------
# 2번째 풀이
# '밟지 않는 계단'의 최소값을 구하여 푼다.
# d 테이블을 1차원 리스트로 만들어 풀 수 있다.
def dp(n, s):
    # 1. 테이블 정의하기
    # d[i] : i번째까지 올라섰을 때 밟지 않은 계단들의 합의 최소(단, i번째 계단은 밟지 않는다.)
    d = [0] * (n+4)
    
    # 2. 점화식 찾기
    # d[k] = s[k] + min(d[k-2], d[k-3])
    
    # 3. 초기값 정하기
    d[1] = s[1]
    d[2] = s[2]
    d[3] = s[3]

    # 예외처리 : n이 3 이하인 경우, 바로 리턴
    if n <= 3:
        return d[n]
    
    for i in range(4, n+1):
        d[i] = s[i] + min(d[i-2], d[i-3])
        
    return d[n]

# 입력
n = int(input())
s = []
s.append(0)
for _ in range(n):
    s.append(int(input()))

# 출력
if n <= 2:
    print(sum(s))
else:
    print(sum(s) - min(dp(n-1, s), dp(n-2, s)))
