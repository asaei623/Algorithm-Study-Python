from collections import deque

def bfs(start):
    date = 1
    # 모든 토마토가 익어있다면 0을 출력 => 모든 토마토가 익어있다면 자연스럽게 0이 출력된다.
    # if len(start) == n*m: 이 코드는 -1인 칸을 고려하지 못한다.
    #    return 0
    
    # 여러 시작점을 큐에 넣고 bfs를 시작한다.
    q = deque(start)
    
    # 큐가 빌 때까지 반복한다.
    while q:
        curx, cury = q.popleft()
        # 인접한 곳 중 익지 않은 토마토(0)이 있으면 큐에 넣는다.
        for i in range(4):
            nx = dx[i] + curx
            ny = dy[i] + cury
            
            if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                q.append([nx, ny])
                # 토마토의 값을 익기까지 걸린 날짜 값으로 대체한다.
                box[ny][nx] = box[cury][curx] + 1
                date = max(box[ny][nx], date)

    # 익지 못한 토마토가 있으면 -1을 출력    
    # 아래 코드는 2차원 배열에서 동작하지 않는다.
    # if 0 in box:
    #    return -1
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
            
    # 익지 못한 토마토가 없으면 마지막 토마토가 익은 날짜를 출력(날짜가 1부터 시작하므로 1을 빼준다)
    return date-1

# 입력
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# 변수들
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 익은 토마토의 좌표를 구해 bfs 시작점으로 넘긴다.
start= []

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            start.append([j, i])
            

# 출력
print(bfs(start))
