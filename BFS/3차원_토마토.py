from collections import deque

def bfs(start):
    date = 1
    
    # 여러 시작점을 큐에 넣고 bfs를 시작한다.
    q = deque(start)
    
    # 큐가 빌 때까지 반복한다.
    while q:
        curx, cury, curh = q.popleft()
        # 인접한 곳 중 익지 않은 토마토(0)이 있으면 큐에 넣는다.
        for i in range(6):
            nx = dx[i] + curx
            ny = dy[i] + cury
            nh = dh[i] + curh
            
            if 0 <= nx < m and 0 <= ny < n and 0 <= nh < h and boxes[nh][ny][nx] == 0:
                q.append([nx, ny, nh])
                # 토마토의 값을 익기까지 걸린 날짜 값으로 대체한다.
                boxes[nh][ny][nx] = boxes[curh][cury][curx] + 1
                date = boxes[nh][ny][nx]

    # 익지 못한 토마토가 있으면 -1을 출력
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if boxes[k][i][j] == 0:
                    return -1
            
    # 익지 못한 토마토가 없으면 마지막 토마토가 익은 날짜를 출력(날짜가 1부터 시작하므로 1을 빼준다)
    return date-1

# 입력
m, n, h = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
boxes = [[list(row) for row in box] for _ in range(h)] # 깊은 복사를 해야 각 행들이 독립적으로 수정된다.

# 변수들
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

# 익은 토마토의 좌표를 구해 bfs 시작점으로 넘긴다.
start= []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:
                start.append([j, i, k])
            

# 출력
print(bfs(start))
