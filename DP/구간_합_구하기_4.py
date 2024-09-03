# 입력
n, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 1. 테이블 정의하기
d = [0] * (n + 1)
for i in range(1, n+1):
    d[i] = d[i-1] + n_list[i-1]

# 2. 점화식 찾기
# n_list[i] + n_list[i+1] + ... + n[j] = d[j] - d[i-1]
for _ in range(m):
    i, j = map(int, input().split())
    # 출력
    print(d[j] - d[i-1])
