from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 노드들을 방문할 때 거리를 기록한다.
    d = {(x, y):1}
    # 시작 노드 방문 처리 후 큐에 넣는다.
    maze[x][y] = 0
    q = deque([(x, y)])

    while q:
        curx, cury = q.popleft()
        curd = d[(curx, cury)] # 현재 원소의 거리
        
        # 상하좌우 원소 중 1인 원소는 방문 처리 후 큐에 넣는다. 
        for i in range(4):
            nx = dx[i] + curx
            ny = dy[i] + cury
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                q.append((nx, ny))
                # 거리를 기록한다.
                d[(nx, ny)] = curd + 1
        
    # 모든 노드들을 방문하고 나면 마지막 노드의 거리를 리턴한다.
    return d[(n-1, m-1)]


# 입력
n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

#출력
print(bfs(0, 0))
